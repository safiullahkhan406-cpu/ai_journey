import json
import os
FILE_NAME = "expenses.json"
def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []
def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)
def add_expense(expenses):
    title = input("Enter expense name: ").strip()
    category = input("Enter category: ").strip()
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount!")
        return
    if not title or not category or amount <= 0:
        print("Enter valid expense details!")
        return
    expense = {
        "id": max(
            (item.get("id", 0) for item in expenses),
            default=0
        ) + 1,
        "title": title,
        "category": category,
        "amount": amount
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")
def view_expenses(expenses):
    if not expenses:
        print("No expenses found!")
        return
    for expense in expenses:
        print(
            f"ID: {expense['id']} | "
            f"Title: {expense['title']} | "
            f"Category: {expense['category']} | "
            f"Amount: Rs. {expense['amount']:.2f}"
        )
def show_total(expenses):
    total = sum(expense["amount"] for expense in expenses)
    print(f"Total expenses: Rs. {total:.2f}")
def search_by_category(expenses):
    category = input("Enter category to search: ").strip().lower()
    results = [
        expense for expense in expenses
        if expense["category"].lower() == category
    ]
    if results:
        for expense in results:
            print(
                f"{expense['title']} - "
                f"Rs. {expense['amount']:.2f}"
            )
    else:
        print("No expenses found in this category!")
def main():
    expenses = load_expenses()
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total")
        print("4. Search by Category")
        print("5. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            show_total(expenses)
        elif choice == "4":
            search_by_category(expenses)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Select 1 to 5.")
if __name__ == "__main__":
    main()
    