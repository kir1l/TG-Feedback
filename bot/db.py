# bot/db.py
import sqlite3
from bot.config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bot_subscribers (
            id INTEGER PRIMARY KEY
        )
    ''')
    conn.commit()
    conn.close()

def add_subscriber(user_id: int):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO bot_subscribers (id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def get_subscribers() -> list:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM bot_subscribers")
    rows = cursor.fetchall()
    conn.close()
    return [row[0] for row in rows]
