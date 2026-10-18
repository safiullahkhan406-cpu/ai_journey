import json
import os
FILE_NAME = "customers.json"
def load_customers():
    """Load customer records from the JSON file."""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        print("Warning: Customer file contains invalid JSON.")
        return []
def save_customers(customers):
    """Save customer records to the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(customers, file, indent=4)
def add_customer():
    """Add a new customer record."""
    customers = load_customers()
    name = input("Enter customer name: ").strip()
    city = input("Enter customer city: ").strip()
    if not name or not city:
        print("Error: Name and city cannot be empty.")
        return
    customer = {
        "name": name,
        "city": city
    }
    customers.append(customer)
    save_customers(customers)
    print(f"Success: Customer '{name}' added successfully!")
def show_customers():
    """Display all saved customer records."""
    customers = load_customers()
    if not customers:
        print("No customers found.")
        return
    print("\n--- Customer Records ---")
    for number, customer in enumerate(customers, start=1):
        print(
            f"{number}. Name: {customer['name']} | "
            f"City: {customer['city']}"
        )
def search_customer():
    """Search for customers by name."""
    customers = load_customers()
    if not customers:
        print("No customers available to search.")
        return
    name = input("Enter customer name to search: ").strip()
    found_customers = [
        customer
        for customer in customers
        if customer["name"].lower() == name.lower()
    ]
    if found_customers:
        print("\n--- Search Results ---")
        for customer in found_customers:
            print(f"Name: {customer['name']} | City: {customer['city']}")
    else:
        print(f"No customer found with the name '{name}'.")
def main():
    """Run the customer management application."""
    while True:
        print("\n===== Customer Management System =====")
        print("1. Add Customer")
        print("2. Show All Customers")
        print("3. Search Customer")
        print("4. Exit")
        choice = input("Choose an option (1-4): ").strip()
        if choice == "1":
            add_customer()
        elif choice == "2":
            show_customers()
        elif choice == "3":
            search_customer()
        elif choice == "4":
            print("Thank you for using Customer Management System!")
            break
        else:
            print("Invalid option. Please choose between 1 and 4.")
if __name__ == "__main__":
    main()
    