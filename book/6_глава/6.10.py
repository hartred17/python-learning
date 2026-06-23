favourite_numbers = {
    'andrey': [67, 76],
    'egor': [80, 100, 118],
    'kristina': [52, 13],
    'ilia': [17, 23, 67],
    'anton': [69, 89],
}

for person, numbers in favourite_numbers.items():
    print(f"{person.title()}'s favourite numbers:")
    for number in numbers:
        print(f"  {number}")
