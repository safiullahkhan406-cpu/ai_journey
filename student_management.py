#Student Database Management System
import sqlite3
# Database connection
connection = sqlite3.connect("students.db")
cursor = connection.cursor()
# Students table create karo
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    course TEXT NOT NULL
)
""")
connection.commit()
# Student add karo
def add_student():
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    course = input("Enter course: ")
    cursor.execute("""
    INSERT INTO students (name, age, course)
    VALUES (?, ?, ?)
    """, (name, age, course))
    connection.commit()
    print("Student added successfully!")
# All students show karo
def show_students():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if not students:
        print("No students found!")
        return
    for student in students:
        print(student)
# Student search karo
def search_student():
    name = input("Enter student name: ")
    cursor.execute(
        "SELECT * FROM students WHERE name = ?",
        (name,)
    )
    student = cursor.fetchall()
    if student:
        for record in student:
            print(record)
    else:
        print("Student not found!")
# Student update karo
def update_student():
    student_id = int(input("Enter student ID: "))
    new_course = input("Enter new course: ")
    cursor.execute("""
    UPDATE students
    SET course = ?
    WHERE id = ?
    """, (new_course, student_id))
    connection.commit()
    if cursor.rowcount > 0:
        print("Student updated successfully!")
    else:
        print("Student not found!")
# Student delete karo
def delete_student():
    student_id = int(input("Enter student ID: "))
    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    connection.commit()
    if cursor.rowcount > 0:
        print("Student deleted successfully!")
    else:
        print("Student not found!")
# Main menu
def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            show_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Program closed!")
            break
        else:
            print("Invalid choice!")
if __name__ == "__main__":
    try:
        main()
    finally:
        connection.close()
        