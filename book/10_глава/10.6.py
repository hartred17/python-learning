print("Напишите мне 2 числа и я сложу их: ")

first_number = input("\nПервое число: ")

second_number = input('\nВторое число: ')

try:
    answer = int(first_number) + int(second_number)
except ValueError:
    print("Вы можете использовать только числа!")
else:
    print(f"\nСумма: {answer}")