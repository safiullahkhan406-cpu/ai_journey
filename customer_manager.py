import json
import os
# File used to store customer records
FILE_NAME = "customers.json"
def load_customers():
    # Check whether the file exists
    if not os.path.exists(FILE_NAME):
        return []
    try:
        # Open the file in read mode
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        # Return an empty list if the file is invalid
        return []
def save_customers(customers):
    # Open the file in write mode
    with open(FILE_NAME, "w") as file:
        json.dump(customers, file, indent=4)
def add_customer(customers):
    # Get customer information from the user
    name = input("Enter customer name: ").strip()
    city = input("Enter customer city: ").strip()
    # Check that both fields contain information
    if not name or not city:
        print("Error: Name and city cannot be empty.")
        return
    # Create a new customer dictionary
    customer = {
        "id": max((c.get("id", 0) for c in customers), default=0) + 1,
        "name": name,
        "city": city
    }
    # Add the customer to the list
    customers.append(customer)
    # Save the updated list
    save_customers(customers)
    print("Customer added successfully!")
def show_customers(customers):
    # Check whether any customers exist
    if not customers:
        print("No customers found.")
        return
    # Display all customer records
    for customer in customers:
        print(
            f"ID: {customer.get('id')}, "
            f"Name: {customer.get('name')}, "
            f"City: {customer.get('city')}"
        )
def search_customer(customers):
    # Get the name to search for
    name = input("Enter customer name to search: ").strip().lower()
    # Find matching customers
    found = False
    for customer in customers:
        if customer.get("name", "").lower() == name:
            print("Customer found:")
            print(customer)
            found = True
    if not found:
        print("Customer not found.")
def main():
    # Load saved customers when the program starts
    customers = load_customers()
    while True:
        print("\n--- Customer Management System ---")
        print("1. Add Customer")
        print("2. Show All Customers")
        print("3. Search Customer")
        print("4. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_customer(customers)
        elif choice == "2":
            show_customers(customers)
        elif choice == "3":
            search_customer(customers)
        elif choice == "4":
            print("Program closed.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
    
