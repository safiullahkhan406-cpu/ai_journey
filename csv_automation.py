# Day 21 - CSV Automation Project

# CSV module import kiya
import csv

# Customers ka data
customers = [
    {"name": "Ali", "age": 25, "city": "Karachi"},
    {"name": "Ahmed", "age": 30, "city": "Lahore"},
    {"name": "Safi", "age": 27, "city": "Karachi"},
    {"name": "Usman", "age": 22, "city": "Islamabad"},
    {"name": "Bilal", "age": 28, "city": "Karachi"}
]

# CSV file mein customers save karna
with open("customers.csv", "w", newline="") as file:

    # CSV writer create kiya
    writer = csv.DictWriter(
        file,
        fieldnames=["name", "age", "city"]
    )

    # Columns ke names likhe
    writer.writeheader()

    # Customers ka data save kiya
    writer.writerows(customers)


# CSV file se data read karna
with open("customers.csv", "r") as file:

    # CSV reader create kiya
    reader = csv.DictReader(file)

    # Sab customers ki list
    all_customers = list(reader)


# Karachi ke customers filter karna
karachi_customers = [
    customer for customer in all_customers
    if customer["city"] == "Karachi"
]


# Total customers count karna
total_customers = len(all_customers)

# Karachi customers count karna
karachi_count = len(karachi_customers)


# Results display karna
print("\n===== CUSTOMER REPORT =====")

print("Total Customers:", total_customers)

print("\nKarachi Customers:")

for customer in karachi_customers:
    print(customer["name"], "-", customer["city"])

print("\nKarachi Customer Count:", karachi_count)

print("\nCSV Automation Completed!")
