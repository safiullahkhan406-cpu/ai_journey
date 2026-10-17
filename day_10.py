import json
import os
FILE_NAME = "customers.json"
def load_customers():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []
def save_customers(customers):
    with open(FILE_NAME, "w") as file:
        json.dump(customers, file, indent=4)
def add_customer():
    customers = load_customers()
    name = input("Enter customer name: ")
    city = input("Enter customer city: ")
    customer = {
        "name": name,
        "city": city
    }
    customers.append(customer)
    save_customers(customers)
    print("Customer added successfully!")
def show_customers():
    customers = load_customers()
    if not customers:
        print("No customers found.")
        return
    for customer in customers:
        print(f"Name: {customer['name']}, City: {customer['city']}")
while True:
    print("\n1. Add Customer")
    print("2. Show Customers")
    print("3. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        add_customer()
    elif choice == "2":
        show_customers()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
        