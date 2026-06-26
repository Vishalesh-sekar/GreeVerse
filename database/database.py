import sqlite3

def create_database():
    conn = sqlite3.connect("greeverse.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS media(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            path TEXT,
            type TEXT
            )
            """)
    conn.commit()
    conn.close()