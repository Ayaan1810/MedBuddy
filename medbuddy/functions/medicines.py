import sqlite3

def get_all_medicines(user_id):
    conn = sqlite3.connect('medicines.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT medicine_name FROM schedules WHERE user_id = ?', (user_id,))
    medicines = cursor.fetchall()
    
    conn.close()
    return [med[0] for med in medicines]

def medicine_card(name, price, order_link):
    return f"<div class='medicine-card'><h3>{name}</h3><p>Price: {price}</p><a href='{order_link}'>Order</a></div>"
