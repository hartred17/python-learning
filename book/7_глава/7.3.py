number = input("Введите число ")
number = int(number)

if number % 10 == 0:
    print(f"{number} кратно 10")
else:
    print(f"{number} не кратно 10")
