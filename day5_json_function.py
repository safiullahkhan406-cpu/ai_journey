import json
import os
FILE_NAME = "person.json"
# Step 1: Create initial data if file does not exist
def create_file():
    if not os.path.exists(FILE_NAME):
        person = {
            "name": "John",
            "age": 30,
            "city": "Karachi"
        }
        save_data(person)
        print("New JSON file created!")
# Step 2: Load data from JSON file
def load_data():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found!")
        return None
    except json.JSONDecodeError:
        print("JSON file contains invalid data!")
        return None
# Step 3: Save data to JSON file
def save_data(data):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)
        print("Data saved successfully!")
    except OSError as error:
        print("Error saving data:", error)
# Step 4: Update person's age
def update_age(new_age):
    person = load_data()
    if person is None:
        return
    person["age"] = new_age
    save_data(person)
    print("Age updated successfully!")
# Step 5: Add a new field
def add_country(country):
    person = load_data()
    if person is None:
        return
    person["country"] = country
    save_data(person)
    print("Country added successfully!")
# Step 6: Display all data
def show_data():
    person = load_data()
    if person is not None:
        print("\n--- Person Information ---")
        print("Name:", person.get("name", "Not available"))
        print("Age:", person.get("age", "Not available"))
        print("City:", person.get("city", "Not available"))
        print("Country:", person.get("country", "Not available"))
# Step 7: Run the program
def main():
    create_file()
    while True:
        print("\n===== JSON DATA MANAGER =====")
        print("1. Show data")
        print("2. Update age")
        print("3. Add country")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            show_data()
        elif choice == "2":
            try:
                new_age = int(input("Enter new age: "))
                if new_age < 0:
                    print("Age cannot be negative!")
                else:
                    update_age(new_age)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "3":
            country = input("Enter country name: ").strip()
            if country:
                add_country(country)
            else:
                print("Country name cannot be empty!")
        elif choice == "4":
            print("Program closed. Allah Hafiz!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")
if __name__ == "__main__":
    main()
    