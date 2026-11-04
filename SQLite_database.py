# SQLite module import kiya
import sqlite3

# Database connection banaya
connection = sqlite3.connect("customers.db")

# SQL commands ke liye cursor banaya
cursor = connection.cursor()

# Customers table create ki
cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    age INTEGER,
    city TEXT
)
""")

# Changes save ki
connection.commit()

# Database connection close kiya
connection.close()

# Success message
print("Database created!")
