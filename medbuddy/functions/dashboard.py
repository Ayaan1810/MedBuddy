import sqlite3
from datetime import datetime, timedelta

def fetch_user_schedule(user_id):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    
    cursor.execute('''
    SELECT medicine_name, hours, minutes, halftime FROM schedules 
    WHERE user_id = ? AND date(start_date) <= date('now') AND date(end_date) >= date('now')
    ''', (user_id,))
    schedules = cursor.fetchall()
    
    upcoming = {}
    completed = {}
    
    now = datetime.now()
    current_time = now.strftime("%H:%M")

    for schedule in schedules:
        medicine_name, hours, minutes, halftime = schedule
        dose_time = f"{hours}:{minutes} {halftime}"
        if dose_time > current_time:
            upcoming[medicine_name] = dose_time
        else:
            completed[medicine_name] = dose_time
            
    conn.close()
    return upcoming, completed

def today_card(medicine_name, dose_time):
    return f"<div class='card'><h3>{medicine_name}</h3><p>Next Dose: {dose_time}</p></div>"

def tomorrow_card(medicine_name, dose_time):
    return f"<div class='card'><h3>{medicine_name}</h3><p>Tomorrow's Dose: {dose_time}</p></div>"

def day_after_card(medicine_name, dose_time):
    return f"<div class='card'><h3>{medicine_name}</h3><p>Day After Dose: {dose_time}</p></div>"
