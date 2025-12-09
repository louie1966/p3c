import requests

response = requests.get("http://api.open-notify.org/astros.json")

data = response.json()

# print(data)

print(f"There are {data['number']} people in space right now.")
for person in data['people']:
    print(f"{person['name']} is on the {person['craft']}")          