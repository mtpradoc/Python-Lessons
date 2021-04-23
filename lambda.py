people = [
    {"name": "Carlos", "house": "Sigma"},
    {"name": "Pedro", "house": "Beta"},
    {"name": "Juan", "house": "Epsilon"}
]

people.sort(key=lambda person: person["name"])

print(people)