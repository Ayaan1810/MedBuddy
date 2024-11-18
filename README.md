# MedBuddy

Contributors: Bhanvi Nayer , Ayaan Edward
 Stay on Track with Your Medication
Here's a `README.md` template for your **Medicine Reminder App** project. You can modify the content as needed based on the specific features of your project:

---

The **Medicine Reminder App** is a Flask-based web application that helps users manage their medicine schedule, upload prescriptions, and receive notifications for upcoming doses. It includes user authentication, prescription uploads, and scheduling of medicines to ensure timely intake.

## Features

- **User Authentication**: Secure login and signup system to manage personalized data.
- **Medicine Scheduling**: Schedule medicines with customizable times and receive reminders for upcoming doses.
- **Prescription Management**: Upload, view, and manage prescriptions in various formats like PDF, JPG, PNG.
- **Dashboard**: Overview of upcoming doses, prescriptions, and completed doses.
- **Responsive UI**: Modern user interface with mobile responsiveness.
- **Notifications**: Alerts to remind users about their scheduled medicines.


### Prerequisites

- Python 3.x
- Flask
- SQLite (or any database of your choice)
- Git (optional for version control)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/medicine-reminder-app.git
   cd medicine-reminder-app
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database:**
   Initialize the database by running the database initialization script.
   ```bash
   python init_db.py
   ```

5. **Run the Flask app:**
   ```bash
   flask run
   ```
   The app will be available at `http://127.0.0.1:5000`.

## Usage

1. **Signup/Login:**
   - New users can sign up using their name, email, contact details, and password.
   - Existing users can log in using their email and password.
   
2. **Add a Prescription:**
   - Go to the **Prescriptions** section.
   - Click on **Add Prescription** to upload a prescription file.

3. **Manage Medicine Schedule:**
   - Navigate to the **Schedule** section to view, add, or edit medicine schedules.
   - You can define the time, start date, and end date for each medicine schedule.

4. **Dashboard:**
   - View your upcoming doses, completed doses, and uploaded prescriptions on the main dashboard.

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Python (Flask)
- **Database**: SQLite (or any other preferred database)
- **Version Control**: Git & GitHub

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

