from random import choice

data = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e')

winning_numbers = []

while len(winning_numbers) < 4:
    pulled_numbers = choice(data)

    if pulled_numbers not in winning_numbers:
        print(f"Выпало: {pulled_numbers}")
        winning_numbers.append(pulled_numbers)

print(f"Выйгрышный билет: {winning_numbers}")
