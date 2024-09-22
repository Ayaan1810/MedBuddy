import sqlite3

import sqlite3
from datetime import datetime, timedelta


def get_schedule(user_id):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    
    # Fetch all upcoming schedules
    cursor.execute('''
    SELECT * FROM schedules WHERE user_id = ? AND date(start_date) >= date('now')
    ''', (user_id,))
    schedules = cursor.fetchall()

    upcoming_count = len(schedules)

    # Prepare data for today's schedule
    today_schedules = [s for s in schedules if s[6] == datetime.now().strftime("%Y-%m-%d")]
    today_card_html = ''.join(f'<div class="card"><h3>{s[2]}</h3><p>{s[3]:02}:{s[4]:02} {s[5]}</p></div>' for s in today_schedules)

    # Prepare data for calendar events
    calendar_events = []
    for schedule in schedules:
        event = {
            'title': schedule[2],  # Medicine name
            'start': f"{schedule[6]}T{schedule[3]:02}:{schedule[4]:02}:00",  # Start time
            'end': f"{schedule[6]}T{schedule[3]:02}:{schedule[4]:02}:00",    # End time (you might want to adjust this)
        }
        calendar_events.append(event)

    conn.close()

    return upcoming_count, today_card_html, calendar_events

from datetime import datetime, timedelta
def mark_dose_taken(user_id, dose):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()

    # Update the status of the medicine dose as taken
    cursor.execute('''
        UPDATE schedules
        SET status = 'taken'  -- Assuming there's a status column in your schedules table
        WHERE user_id = ? AND medicine_name = ?
    ''', (user_id, dose))

    conn.commit()
    conn.close()


from datetime import datetime, timedelta

def get_dosage_dates(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    dates = []

    # Default frequency: every day
    days = 1

    while start <= end:
        dates.append(start.strftime("%Y-%m-%d"))
        start += timedelta(days=days)
        
    return dates





def add_schedule(user_id, medicine_name, hours, minutes, halftime, start_date, end_date):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO schedules (user_id, medicine_name, hours, minutes, halftime, start_date, end_date)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, medicine_name, hours, minutes, halftime, start_date, end_date))
    conn.commit()
    conn.close()
    

