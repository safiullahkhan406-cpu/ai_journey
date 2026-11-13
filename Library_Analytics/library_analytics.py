import sqlite3

# Database connection
connection = sqlite3.connect("day31_library.db")
cursor = connection.cursor()

# Books table create karo
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    category TEXT NOT NULL,
    status TEXT DEFAULT 'Available'
)
""")

# Members table create karo
cursor.execute("""
CREATE TABLE IF NOT EXISTS members (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
""")
# Existing table ke columns check karo
columns = [column[1] for column in cursor.execute(
    "PRAGMA table_info(books)"
).fetchall()]

# Missing category column add karo
if "category" not in columns:
    cursor.execute("ALTER TABLE books ADD COLUMN category TEXT")

# Missing status column add karo
if "status" not in columns:
    cursor.execute(
        "ALTER TABLE books ADD COLUMN status TEXT DEFAULT 'Available'"
    )

# Sample books insert karo
cursor.execute("SELECT COUNT(*) FROM books")

if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO books (title, author, category, status)
    VALUES (?, ?, ?, ?)
    """, [
        ("Python Basics", "John Smith", "Programming", "Available"),
        ("Learning SQL", "David Lee", "Programming", "Issued"),
        ("The Alchemist", "Paulo Coelho", "Novel", "Available"),
        ("Atomic Habits", "James Clear", "Self Help", "Issued"),
        ("Rich Dad Poor Dad", "Robert Kiyosaki", "Finance", "Available")
    ])

# Sample members insert karo
cursor.execute("SELECT COUNT(*) FROM members")

if cursor.fetchone()[0] == 0:
    cursor.executemany("""
    INSERT INTO members (name)
    VALUES (?)
    """, [
        ("Ali",),
        ("Ahmed",),
        ("Usman",),
        ("Bilal",)
    ])

connection.commit()

# 1. Total books
cursor.execute("SELECT COUNT(*) FROM books")
print("Total Books:", cursor.fetchone()[0])

# 2. Total members
cursor.execute("SELECT COUNT(*) FROM members")
print("Total Members:", cursor.fetchone()[0])

# 3. Available books
cursor.execute("""
SELECT COUNT(*) FROM books
WHERE status = 'Available'
""")
print("Available Books:", cursor.fetchone()[0])

# 4. Issued books
cursor.execute("""
SELECT COUNT(*) FROM books
WHERE status = 'Issued'
""")
print("Issued Books:", cursor.fetchone()[0])

# 5. Issued books list
cursor.execute("""
SELECT title FROM books
WHERE status = 'Issued'
""")

print("\nIssued Books:")
for book in cursor.fetchall():
    print(book[0])

# 6. Programming books
cursor.execute("""
SELECT title, category FROM books
WHERE category = 'Programming'
""")

print("\nProgramming Books:")
for book in cursor.fetchall():
    print(book[0], "-", book[1])

# 7. Books sorting
cursor.execute("""
SELECT title FROM books
ORDER BY title ASC
""")

print("\nBooks Alphabetical Order:")
for book in cursor.fetchall():
    print(book[0])

# 8. Category-wise report
cursor.execute("""
SELECT category, COUNT(*)
FROM books
GROUP BY category
""")

print("\nCategory-wise Report:")
for category, total in cursor.fetchall():
    print(category, ":", total)

connection.close()

print("\nLibrary Analytics Completed!")

