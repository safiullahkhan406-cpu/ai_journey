import json

person = {"name": "John", "age": 30, "city": "New York"}

# File mein data likhna
with open('person.json', 'w') as file:
    json.dump(person, file, indent=4)
    print("JSON data has been written to person.json")

# File se data padhna
with open('person.json', 'r') as file:
    try:
        saved_person = json.load(file)
        print(saved_person)
    except json.JSONDecodeError:
        print("File empty .")
        name = ""
        city = ""
    else:
        name = saved_person["name"]
        city = saved_person["city"]
        print("city:", city)