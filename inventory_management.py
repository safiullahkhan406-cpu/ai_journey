import sqlite3

# Database connection
connection = sqlite3.connect("inventory.db")

# SQL commands ke liye cursor
cursor = connection.cursor()


# Database table create ki
def create_table():

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
    """)

    connection.commit()


# Price input validation
def get_price():

    while True:
        try:
            price = float(input("Enter price: "))

            if price < 0:
                print("Price negative nahi ho sakti!")
                continue

            return price

        except ValueError:
            print("Please valid number enter karein!")


# Quantity input validation
def get_quantity():

    while True:
        try:
            quantity = int(input("Enter quantity: "))

            if quantity < 0:
                print("Quantity negative nahi ho sakti!")
                continue

            return quantity

        except ValueError:
            print("Please valid integer enter karein!")


# Product add karne ka function
def add_product():

    name = input("Enter product name: ").strip()

    if not name:
        print("Product name required hai!")
        return

    price = get_price()
    quantity = get_quantity()

    cursor.execute("""
    INSERT INTO products (name, price, quantity)
    VALUES (?, ?, ?)
    """, (name, price, quantity))

    connection.commit()

    print("Product successfully added!")


# Tamam products show karne ka function
def show_products():

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    if not products:
        print("No products found!")
        return

    print("\nID | Name | Price | Quantity")
    print("-" * 40)

    for product in products:
        print(
            product[0],
            product[1],
            product[2],
            product[3],
            sep=" | "
        )


# Product search karne ka function
def search_product():

    name = input("Enter product name: ").strip()

    cursor.execute("""
    SELECT * FROM products
    WHERE name LIKE ?
    """, (f"%{name}%",))

    products = cursor.fetchall()

    if products:
        for product in products:
            print(product)
    else:
        print("Product not found!")


# Product update karne ka function
def update_product():

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    cursor.execute("""
    SELECT * FROM products
    WHERE id = ?
    """, (product_id,))

    product = cursor.fetchone()

    if product is None:
        print("Product not found!")
        return

    print("Current Product:", product)

    print("1. Update Price")
    print("2. Update Quantity")

    choice = input("Enter choice: ")

    if choice == "1":

        price = get_price()

        cursor.execute("""
        UPDATE products
        SET price = ?
        WHERE id = ?
        """, (price, product_id))

    elif choice == "2":

        quantity = get_quantity()

        cursor.execute("""
        UPDATE products
        SET quantity = ?
        WHERE id = ?
        """, (quantity, product_id))

    else:
        print("Invalid choice!")
        return

    connection.commit()

    print("Product updated successfully!")


# Product delete karne ka function
def delete_product():

    try:
        product_id = int(input("Enter product ID: "))
    except ValueError:
        print("Invalid ID!")
        return

    cursor.execute("""
    SELECT * FROM products
    WHERE id = ?
    """, (product_id,))

    product = cursor.fetchone()

    if product is None:
        print("Product not found!")
        return

    print("Selected Product:", product)

    confirm = input("Delete this product? (yes/no): ").lower()

    if confirm == "yes":

        cursor.execute("""
        DELETE FROM products
        WHERE id = ?
        """, (product_id,))

        connection.commit()

        print("Product deleted successfully!")

    else:
        print("Delete cancelled!")


# Low stock check karne ka function
def low_stock_alert():

    cursor.execute("""
    SELECT * FROM products
    WHERE quantity <= 5
    """)

    products = cursor.fetchall()

    if products:
        print("\nLOW STOCK ALERT!")

        for product in products:
            print(product)

    else:
        print("All products have sufficient stock!")


# Inventory summary
def inventory_summary():

    cursor.execute("""
    SELECT
        COUNT(*),
        SUM(quantity),
        SUM(price * quantity)
    FROM products
    """)

    summary = cursor.fetchone()

    print("\n===== INVENTORY SUMMARY =====")

    print("Total Products:", summary[0])
    print("Total Stock:", summary[1] or 0)
    print("Total Stock Value:", summary[2] or 0)


# Main menu
def main():

    create_table()

    while True:

        print("\n===== INVENTORY MANAGEMENT =====")

        print("1. Add Product")
        print("2. View Products")
        print("3. Search Product")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Low Stock Alert")
        print("7. Inventory Summary")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_product()

        elif choice == "2":
            show_products()

        elif choice == "3":
            search_product()

        elif choice == "4":
            update_product()

        elif choice == "5":
            delete_product()

        elif choice == "6":
            low_stock_alert()

        elif choice == "7":
            inventory_summary()

        elif choice == "8":
            print("Inventory System Closed!")
            break

        else:
            print("Invalid choice! Try again.")


# Program start
try:
    main()

except sqlite3.Error as error:
    print("Database Error:", error)

finally:
    connection.close()
    