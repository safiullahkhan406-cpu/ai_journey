# Day 29 - Shop Sales & Profit Tracker

import sqlite3

# Database connection
connection = sqlite3.connect("sales.db")
cursor = connection.cursor()


# Sales table create karo
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    cost_price REAL NOT NULL,
    selling_price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
""")

connection.commit()


# New sale add karo
def add_sale():

    product = input("Product Name: ")

    cost_price = float(input("Cost Price: "))

    selling_price = float(input("Selling Price: "))

    quantity = int(input("Quantity: "))

    cursor.execute("""
    INSERT INTO sales
    (product, cost_price, selling_price, quantity)
    VALUES (?, ?, ?, ?)
    """, (product, cost_price, selling_price, quantity))

    connection.commit()

    print("Sale Added Successfully!")


# All sales display karo
def view_sales():

    cursor.execute("SELECT * FROM sales")

    records = cursor.fetchall()

    for record in records:
        print(record)


# Total revenue calculate karo
def total_revenue():

    cursor.execute("""
    SELECT SUM(selling_price * quantity)
    FROM sales
    """)

    result = cursor.fetchone()

    print("Total Revenue:", result[0] or 0)


# Total profit calculate karo
def total_profit():

    cursor.execute("""
    SELECT SUM((selling_price - cost_price) * quantity)
    FROM sales
    """)

    result = cursor.fetchone()

    print("Total Profit:", result[0] or 0)


# Product search karo
def search_product():

    name = input("Enter Product Name: ")

    cursor.execute("""
    SELECT * FROM sales
    WHERE product LIKE ?
    """, ('%' + name + '%',))

    records = cursor.fetchall()

    for record in records:
        print(record)

    if not records:
        print("Product Not Found!")


# Main menu
while True:

    print("\n===== SHOP SALES TRACKER =====")

    print("1. Add Sale")
    print("2. View Sales")
    print("3. Total Revenue")
    print("4. Total Profit")
    print("5. Search Product")
    print("6. Exit")

    choice = input("Choose Option: ")

    if choice == "1":
        add_sale()

    elif choice == "2":
        view_sales()

    elif choice == "3":
        total_revenue()

    elif choice == "4":
        total_profit()

    elif choice == "5":
        search_product()

    elif choice == "6":
        connection.close()
        print("Program Closed!")
        break

    else:
        print("Invalid Choice!")
        