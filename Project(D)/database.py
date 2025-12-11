# database.py
import sqlite3

def connect():
    return sqlite3.connect("horoscope.db", check_same_thread=False)

def create_tables():
    db = connect()
    cur = db.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            zodiac TEXT
        )
    """)
    db.commit()
    db.close()

def set_user_zodiac(user_id, zod):
    db = connect()
    cur = db.cursor()
    cur.execute("INSERT OR REPLACE INTO users (user_id, zodiac) VALUES (?, ?)", (user_id, zod))
    db.commit()
    db.close()

def get_user_zodiac(user_id):
    db = connect()
    cur = db.cursor()
    cur.execute("SELECT zodiac FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    db.close()
    return row[0] if row else None