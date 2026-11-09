#Student Database Analytics

import sqlite3

# Database connection
connection = sqlite3.connect("students.db")
cursor = connection.cursor()


# Total students count karo
def total_students():

    cursor.execute("""
    SELECT COUNT(*) FROM students
    """)

    result = cursor.fetchone()

    print("Total Students:", result[0])


# Average age calculate karo
def average_age():

    cursor.execute("""
    SELECT AVG(age) FROM students
    """)

    result = cursor.fetchone()

    print("Average Age:", result[0])


# Course-wise students count karo
def course_report():

    cursor.execute("""
    SELECT course, COUNT(*)
    FROM students
    GROUP BY course
    """)

    results = cursor.fetchall()

    for course in results:
        print(course[0], ":", course[1])


# Students ko age ke hisaab se sort karo
def sorted_students():

    cursor.execute("""
    SELECT name, age
    FROM students
    ORDER BY age DESC
    """)

    results = cursor.fetchall()

    for student in results:
        print(student)


# Youngest aur oldest student
def age_report():

    cursor.execute("""
    SELECT MIN(age), MAX(age)
    FROM students
    """)

    result = cursor.fetchone()

    print("Youngest Age:", result[0])
    print("Oldest Age:", result[1])


# Main menu
def main():

    while True:

        print("\n===== STUDENT ANALYTICS =====")
        print("1. Total Students")
        print("2. Average Age")
        print("3. Course Report")
        print("4. Sort Students")
        print("5. Age Report")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            total_students()

        elif choice == "2":
            average_age()

        elif choice == "3":
            course_report()

        elif choice == "4":
            sorted_students()

        elif choice == "5":
            age_report()

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
        