countries = ["Tokyo", "German", "USA", "Norway", "Argentina"]
print("Исходный порядок:")
print(countries)

print("\nАлфавитный порядок:")
print(sorted(countries))

print("\nИсходный порядок:")
print(countries)

print("\nОбратный алфавитный:")
print(sorted(countries, reverse=True))

print("\nИсходный порядок:")
print(countries)

countries.reverse()
print("\nОбратный порядок:")
print(countries)

countries.reverse()
print("\nИсходный порядок:")
print(countries)

countries.sort()
print("\nАлфавитный порядок:")
print(countries)

countries.sort()
print("\nОбратный алфавитный:")
print(countries)
