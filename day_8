import json
import os

FILE_NAME = "customers.json"


def add_customer():
    name = input("Enter customer name: ")
    city = input("Enter customer city: ")

    customer = {
        "name": name,
        "city": city
    }

    customers = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            customers = json.load(file)

    customers.append(customer)

    with open(FILE_NAME, "w") as file:
        json.dump(customers, file, indent=4)

    print("Customer saved successfully!")


add_customer()
