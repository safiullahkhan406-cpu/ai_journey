import requests

# ==============================
# PUT - Replace the ENTIRE data
# ==============================

put_data = {
    "id": 1,
    "title": "Updated Title",
    "body": "This is completely new data",
    "userId": 1
}

response = requests.put(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=put_data
)

print("PUT Status Code:", response.status_code)
print("PUT Response:", response.json())

print("-" * 40)

# ==============================
# PATCH - Update ONLY one field
# ==============================

patch_data = {
    "title": "Only title changed"
}

response = requests.patch(
    "https://jsonplaceholder.typicode.com/posts/1",
    json=patch_data
)

print("PATCH Status Code:", response.status_code)
print("PATCH Response:", response.json())

