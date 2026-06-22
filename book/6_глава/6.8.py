# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = {
    'name': 'milana',
    'animal_species': "dog",
    'owner': 'masha',
}
pets.append(pet)

pet = {
    'name': 'arnold',
    'animal_species': 'cat',
    'owner': 'yulia',
}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print(f"\nHere's what I know about {pet['name'].title()}:")

    for key, value in pet.items():
        print(f"{key.title()}: {value.title()}")
