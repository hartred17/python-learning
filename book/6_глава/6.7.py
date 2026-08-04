people = [
    {
        'first_name': 'ilia',
        'last_name': 'glok',
        'age': 24,
        'city': 'tyla',
    },
    {
        'first_name': 'anna',
        'last_name': 'smith',
        'age': 28,
        'city': 'london',
    },
    {
        'first_name': 'michael',
        'last_name': 'brown',
        'age': 35,
        'city': 'new york',
    }
    
]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()}"
          f" of {person['city'].title()} is {person['age']} years old")
    