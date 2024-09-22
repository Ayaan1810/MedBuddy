import sqlite3
import bcrypt
def get_db_connection():
    conn = sqlite3.connect('medicines.db')
    conn.row_factory = sqlite3.Row  # Access by column name
    return conn

# Create a new user in the SQLite database
def create_user(name, email, contact, emergency_contact, password):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    try:
        # Hash the password before storing
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        cursor.execute('''
        INSERT INTO users (name, email, contact, emergency_contact, password)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, email, contact, emergency_contact, hashed_password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

# Check if a user with the given email already exists
def check_existing_user(email):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    cursor.execute('SELECT email FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()
    return user is not None

# Verify the user's email and password
def verify_user(email, password):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[5].encode('utf-8')):
        # user[5] is the password column
        return {
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'contact': user[3],
            'emergency_contact': user[4]
        }
    return None

# Add a new user
def add_new_user(name, email, hashed_password, contact, emergency_contact):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    try:
        cursor.execute('''
        INSERT INTO users (name, email, contact, emergency_contact, password)
        VALUES (?, ?, ?, ?, ?)
        ''', (name, email, contact, emergency_contact, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
    return True

# Retrieve a user by email
def get_user_by_email(email):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE email = ?', (email,))
    user = cursor.fetchone()
    conn.close()

    if user:
        return {
            'id': user[0],
            'name': user[1],
            'email': user[2],
            'contact': user[3],
            'emergency_contact': user[4],
            'password': user[5]
        }
    return None
