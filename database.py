import sqlite3

# connect to database
conn = sqlite3.connect("expense.db")

# create cursor
cursor = conn.cursor()

# create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    amount REAL,
    category TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")