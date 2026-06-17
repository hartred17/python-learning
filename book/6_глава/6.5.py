rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'volga': 'russia',
}

for river, country in rivers.items():
    print(f"{river.title()} протекает через {country.title()}")

for river in rivers.keys():
    print(f"{river.title()}")

for country in rivers.values():
    print(f"{country.title()}")
