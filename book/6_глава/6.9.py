favourite_places = {
    'ilia': ['paris', 'moscow', 'tokyo'],
    'anna': ['rome', 'london'],
    'michael': ['seoul', 'osaka'],
}

for person, places in favourite_places.items():
    print(f"{person.title()}'s favourite places:")
    for place in places:
        print(f"- {place.title()}")
