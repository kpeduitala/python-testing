import sqlite3

def setup_database():
    conn = sqlite3.connect('database.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT UNIQUE NOT NULL,
                        password TEXT NOT NULL
                    )''')
    conn.execute('''CREATE TABLE IF NOT EXISTS data (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product TEXT NOT NULL,
                        quantity INTEGER NOT NULL,
                        price REAL NOT NULL
                    )''')
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
    print("Database setup completed.")