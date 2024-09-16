import sqlite3

conn = sqlite3.connect('urls.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS urls (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url TEXT unique,
    title TEXT               
)
''')

conn.commit()
conn.close()

print("Database setup complete")