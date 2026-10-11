import json
import os

# --- 1. Create Data ---
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

file_name = "person.json"

# --- 2. Write Data to JSON File ---
try:
    with open(file_name, 'w') as file:
        json.dump(person, file, indent=4)
    print(f"✅ Data successfully saved to {file_name}.")
except Exception as e:
    print(f"❌ Error saving the file: {e}")

# --- 3. Read Data from JSON File ---
try:
    with open(file_name, 'r') as file:
        saved_person = json.load(file)
    print("📖 Data loaded from file:")
    print(saved_person)
    
    # Step 6: Extract specific data
    print("\n--- Specific Data ---")
    print(f"Name: {saved_person['name']}")
    print(f"City: {saved_person['city']}")
    
except FileNotFoundError:
    print(f"❌ {file_name} not found. Please create the file first.")
except json.JSONDecodeError:
    print("❌ The file is empty or contains invalid JSON data.")

# --- 4. Update Data and Save Back ---
try:
    # Modify the existing data
    saved_person["age"] = 31                  # Update age
    saved_person["country"] = "Pakistan"      # Add new field
    
    # Write the updated data back to the file
    with open(file_name, 'w') as file:
        json.dump(saved_person, file, indent=4)
        
    print("\n🔄 Data successfully updated!")
    print("Updated Data:", saved_person)
    
except Exception as e:
    print(f"❌ Error updating the file: {e}")
    