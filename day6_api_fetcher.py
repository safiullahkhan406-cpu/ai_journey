import requests
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
get_users()
find_user("Leanne Graham")
