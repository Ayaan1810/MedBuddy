from flask import Flask, render_template, request, redirect, url_for, flash, session
from functions.users import create_user, verify_user, get_user_by_email
from functions.scheduler import get_schedule, add_schedule, get_dosage_dates, mark_dose_taken
from functions.prescription import add_prescription, prescription_card, get_prescriptions
from functions.users import check_existing_user, add_new_user
import os
import bcrypt

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        contact = request.form['contact']
        emergency_contact = request.form['emergency_contact']
        password = request.form['password']
        if create_user(name, email, contact, emergency_contact, password):
            flash('User registered successfully!')
            return redirect(url_for('login'))
        else:
            flash('Error registering user.')
    return render_template('signup.html')

@app.route('/signup/verify', methods=['POST'])
def signup_verify():
    if request.method == 'POST':
        data = request.form
        name = data['name']
        email = data['email']
        contact = data['contact']
        emergency_contact = data['emergency_contact']
        password = data['password'].encode()

        # Hash the password
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

        # Check if the user already exists
        if check_existing_user(email):
            flash('User with this email already exists.', 'error')
            return render_template('signup.html')
        else:
            add_new_user(name, email, hashed_password, contact, emergency_contact)
            flash('Signup successful!')
            return redirect('/')

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = verify_user(email, password)
        if user:
            session['user_id'] = user.id
            session['name'] = user.name
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid credentials.')
    return render_template('login.html')

@app.route('/login/verify', methods=['POST'])
def login_verify():
    if request.method == 'POST':
        data = request.form
        email = data['email']
        password = data['password'].encode()

        user = get_user_by_email(email)
        if user and bcrypt.checkpw(password, user['password']):
            session['user_id'] = user['id']
            session['name'] = user['name']
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password.')
            return redirect('/login')

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    upcoming_count, today_card_html, calendar_events = get_schedule(session['user_id'])
    
    return render_template('dashboard.html', name=session['name'], upcoming_count=upcoming_count, today_card_html=today_card_html)


@app.route('/schedule')
def schedule():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    upcoming_card_html, completed_card_html,calendar_events = get_schedule(session['user_id'])
    return render_template('schedule.html', upcoming_card_html=upcoming_card_html, completed_card_html=completed_card_html)



@app.route('/schedule/add', methods=['GET', 'POST'])
def add_medicine():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        medicine_name = request.form['medicine-name']
        hours = request.form['hours']
        minutes = request.form['minutes']
        halftime = request.form['halftime']
        start_date = request.form['start-date']
        end_date = request.form['end-date']
        
        dosage_dates = get_dosage_dates(start_date, end_date)
        
        for date in dosage_dates:
            add_schedule(session['user_id'], medicine_name, hours, minutes, halftime, date, date)  # Use the same date for start and end
        
        return redirect(url_for('dashboard'))
    return render_template('add-medicine.html')



@app.route('/schedule/take_medicine', methods=['POST'])
def take_medicine():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    doses_taken = request.form.getlist('doses')  # Get the list of checked doses
    user_id = session['user_id']
    
    # Here you can mark the doses as taken in the database
    for dose in doses_taken:
        # Add logic to update the medicine status in the database
        mark_dose_taken(user_id, dose)  # You'll need to implement this function

    flash('Doses marked as taken successfully!')
    return redirect(url_for('dashboard'))


@app.route('/prescription')
def prescriptions():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    prescriptions = get_prescriptions(session['user_id'])
    prescription_card_html = [prescription_card(p['file_path'], p['file_path']) for p in prescriptions]

    return render_template('prescriptions.html', prescription_card_html=prescription_card_html)

@app.route('/prescription/add', methods=['GET', 'POST'])
def upload_prescription():  # Renamed to avoid confusion
    if request.method == 'POST':
        if 'prescription-file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['prescription-file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        file_path = os.path.join('path_to_save_files', file.filename)
        file.save(file_path)
        
        add_prescription(file_path, session['user_id'])  # Save prescription info to the database
        flash('Prescription uploaded successfully!')
        return redirect(url_for('prescriptions'))
    return render_template('add-prescription.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('name', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

