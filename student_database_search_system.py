#Student Database Search System

import sqlite3

# Database connection
connection = sqlite3.connect("students.db")
cursor = connection.cursor()


# 1. All students show karo
def show_students():

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    for student in students:
        print(student)


# 2. Name se student search karo
def search_name():

    name = input("Enter student name: ")

    cursor.execute("""
    SELECT * FROM students
    WHERE name LIKE ?
    """, ('%' + name + '%',))

    results = cursor.fetchall()

    for student in results:
        print(student)

    if not results:
        print("Student not found!")


# 3. Course se search karo
def search_course():

    course = input("Enter course: ")

    cursor.execute("""
    SELECT * FROM students
    WHERE course = ?
    """, (course,))

    results = cursor.fetchall()

    for student in results:
        print(student)

    if not results:
        print("No students found!")


# 4. Age range search
def search_age():

    minimum = int(input("Minimum age: "))
    maximum = int(input("Maximum age: "))

    cursor.execute("""
    SELECT * FROM students
    WHERE age BETWEEN ? AND ?
    """, (minimum, maximum))

    results = cursor.fetchall()

    for student in results:
        print(student)

    if not results:
        print("No students found!")


# 5. Students sorting
def sort_students():

    cursor.execute("""
    SELECT * FROM students
    ORDER BY age ASC
    """)

    results = cursor.fetchall()

    for student in results:
        print(student)


# Main menu
def main():

    while True:

        print("\n===== STUDENT SEARCH SYSTEM =====")
        print("1. Show All Students")
        print("2. Search By Name")
        print("3. Search By Course")
        print("4. Search By Age")
        print("5. Sort By Age")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            show_students()

        elif choice == "2":
            search_name()

        elif choice == "3":
            search_course()

        elif choice == "4":
            search_age()

        elif choice == "5":
            sort_students()

        elif choice == "6":
            print("Program Closed!")
            break

        else:
            print("Invalid Choice!")


try:
    main()

finally:
    connection.close()
    