print("Напишите мне 2 числа и я сложу их: ")
print("Enter 'q' to quit")

while True:
    first_number = input("\nПервое число: ")
    if first_number == "q":
        break

    second_number = input("\nВторое число: ")
    if second_number == "q":
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Вы можете использовать только числа!")
    else:
        print(f"\nСумма: {answer}")
