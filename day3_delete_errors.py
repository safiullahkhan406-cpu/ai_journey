import requests
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print("Delete Status Code:",response.status_code)
print("Delete Response:" ,response.json())
response = requests.get('https://jsonplaceholder.typicode.com/posts/1000')
print("Wrong URL Status:",response.status_code)
try:
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1000')
    response.raise_for_status()
    print("Response:", response.json())
except requests.exceptions.HTTPError as e:
    print("HTTP Error:", e)
