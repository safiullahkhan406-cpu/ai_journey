import requests
# Day 7: Get All Users
def get_users():
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        users = response.json()
        print("Total users:", len(users))
        print("\nUser Names:")
        for user in users:
            print(user["name"])
    except requests.exceptions.RequestException as error:
        print("API Error:", error)
# Search User by Name
def find_user(user_name):
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        users = response.json()
        for user in users:
            if user["name"].lower() == user_name.lower():
                print("\nUser Found!")
                print("Name:", user["name"])
                print("Email:", user["email"])
                print("City:", user["address"]["city"])
                return
        print("User not found.")
    except requests.exceptions.RequestException as error:
        print("API Error:", error)
# Search Users by City
def find_users_by_city(city_name):
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        users = response.json()
        found = 0
        print("\nUsers in", city_name, ":")
        for user in users:
            if user["address"]["city"].lower() == city_name.lower():
                print("Name:", user["name"])
                print("City:", user["address"]["city"])
                print("----------------")
                found += 1
        print("Total found:", found)
    except requests.exceptions.RequestException as error:
        print("API Error:", error)
# Run Functions
get_users()
find_user("Leanne Graham")
find_users_by_city("Gwenborough")
