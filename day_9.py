import requests
# Get users from the API
url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url, timeout=10)
response.raise_for_status()
users = response.json()
# Find users from a specific city
def find_users_by_city(city):
    for user in users:
        if user["address"]["city"].lower() == city.lower():
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("City:", user["address"]["city"])
            print("--------------------")
# Search for users from South Christy
find_users_by_city("South Christy")
