import sqlite3

print("prescription.py is loaded")

def create_prescriptions_table():
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS prescriptions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        file_path TEXT NOT NULL
    )
    ''')
    
    conn.commit()
    conn.close()

def get_prescriptions(user_id):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM prescriptions WHERE user_id = ?', (user_id,))
    prescriptions = cursor.fetchall()
    
    conn.close()
    return prescriptions

def add_prescription(file_path, user_id):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    INSERT INTO prescriptions (user_id, file_path) VALUES (?, ?)
    ''', (user_id, file_path))
    conn.commit()
    conn.close()

def prescription_card(name, link):
    return f"<div class='prescription-card'><h3>{name}</h3><a href='{link}'>View Prescription</a></div>"

# Create the prescriptions table
create_prescriptions_table()

# You can test adding a prescription
# add_prescription('path/to/file', 1)

# And retrieving prescriptions for a user
# print(get_prescriptions(1))
