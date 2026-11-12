# Day 30 - Library Management System

import sqlite3
from pathlib import Path

# Database location
db_path = Path(__file__).with_name("library.db")

# Database connection
connection = sqlite3.connect(db_path)
connection.execute("PRAGMA foreign_keys = ON")

cursor = connection.cursor()


# Create Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    total_copies INTEGER NOT NULL,
    available_copies INTEGER NOT NULL
)
""")


# Create Issued Books Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS issued_books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    book_id INTEGER NOT NULL,
    student_name TEXT NOT NULL,
    status TEXT DEFAULT 'Issued',
    FOREIGN KEY (book_id) REFERENCES books(id)
)
""")

connection.commit()


# Add Book Function
def add_book():

    title = input("Enter Book Title: ").strip()
    author = input("Enter Author Name: ").strip()

    try:
        copies = int(input("Enter Total Copies: "))

        if not title or not author or copies <= 0:
            print("Invalid Book Details!")
            return

        cursor.execute("""
        INSERT INTO books
        (title, author, total_copies, available_copies)
        VALUES (?, ?, ?, ?)
        """, (title, author, copies, copies))

        connection.commit()

        print("Book Added Successfully!")

    except ValueError:
        print("Enter a valid number!")


# View Books Function
def view_books():

    cursor.execute("SELECT * FROM books")

    books = cursor.fetchall()

    print("\n===== ALL BOOKS =====")

    if not books:
        print("No Books Available!")
        return

    for book in books:
        print(
            f"ID: {book[0]} | "
            f"Title: {book[1]} | "
            f"Author: {book[2]} | "
            f"Total: {book[3]} | "
            f"Available: {book[4]}"
        )


# Search Book Function
def search_book():

    try:
        book_id = int(input("Enter Book ID: "))

        cursor.execute(
            "SELECT * FROM books WHERE id = ?",
            (book_id,)
        )

        book = cursor.fetchone()

        if book:
            print("\nBook Found:", book)
        else:
            print("Book Not Found!")

    except ValueError:
        print("Invalid Book ID!")


# Update Book Function
def update_book():

    try:
        book_id = int(input("Enter Book ID: "))
        new_copies = int(input("Enter New Total Copies: "))

        cursor.execute(
            "SELECT total_copies, available_copies FROM books WHERE id = ?",
            (book_id,)
        )

        book = cursor.fetchone()

        if not book:
            print("Book Not Found!")
            return

        issued_copies = book[0] - book[1]

        if new_copies < issued_copies or new_copies <= 0:
            print("Invalid Quantity! Check issued copies.")
            return

        available = new_copies - issued_copies

        cursor.execute("""
        UPDATE books
        SET total_copies = ?,
            available_copies = ?
        WHERE id = ?
        """, (new_copies, available, book_id))

        connection.commit()

        print("Book Updated Successfully!")

    except ValueError:
        print("Enter Valid Numbers!")


# Delete Book Function
def delete_book():

    try:
        book_id = int(input("Enter Book ID: "))

        cursor.execute("""
        SELECT COUNT(*) FROM issued_books
        WHERE book_id = ? AND status = 'Issued'
        """, (book_id,))

        issued = cursor.fetchone()[0]

        if issued > 0:
            print("Cannot Delete! Book Is Issued.")
            return

        cursor.execute(
            "DELETE FROM books WHERE id = ?",
            (book_id,)
        )

        connection.commit()

        if cursor.rowcount > 0:
            print("Book Deleted Successfully!")
        else:
            print("Book Not Found!")

    except ValueError:
        print("Invalid Book ID!")


# Issue Book Function
def issue_book():

    try:
        book_id = int(input("Enter Book ID: "))
        student = input("Enter Student Name: ").strip()

        if not student:
            print("Student Name Required!")
            return

        cursor.execute("""
        SELECT available_copies
        FROM books
        WHERE id = ?
        """, (book_id,))

        book = cursor.fetchone()

        if not book:
            print("Book Not Found!")
            return

        if book[0] <= 0:
            print("Book Not Available!")
            return

        cursor.execute("""
        INSERT INTO issued_books (book_id, student_name)
        VALUES (?, ?)
        """, (book_id, student))

        cursor.execute("""
        UPDATE books
        SET available_copies = available_copies - 1
        WHERE id = ?
        """, (book_id,))

        connection.commit()

        print("Book Issued Successfully!")

    except ValueError:
        print("Invalid Book ID!")


# Return Book Function
def return_book():

    try:
        issue_id = int(input("Enter Issue Record ID: "))

        cursor.execute("""
        SELECT book_id
        FROM issued_books
        WHERE id = ? AND status = 'Issued'
        """, (issue_id,))

        record = cursor.fetchone()

        if not record:
            print("Active Issue Record Not Found!")
            return

        book_id = record[0]

        cursor.execute("""
        UPDATE issued_books
        SET status = 'Returned'
        WHERE id = ?
        """, (issue_id,))

        cursor.execute("""
        UPDATE books
        SET available_copies = available_copies + 1
        WHERE id = ?
        """, (book_id,))

        connection.commit()

        print("Book Returned Successfully!")

    except ValueError:
        print("Invalid Issue Record ID!")


# Main Menu
while True:

    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")

    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book")
    print("5. Delete Book")
    print("6. Issue Book")
    print("7. Return Book")
    print("8. Exit")

    choice = input("\nEnter Your Choice: ")

    if choice == "1":
        add_book()

    elif choice == "2":
        view_books()

    elif choice == "3":
        search_book()

    elif choice == "4":
        update_book()

    elif choice == "5":
        delete_book()

    elif choice == "6":
        issue_book()

    elif choice == "7":
        return_book()

    elif choice == "8":
        print("Library Management System Closed!")
        break

    else:
        print("Invalid Choice! Try Again.")


# Close Database
connection.close()
