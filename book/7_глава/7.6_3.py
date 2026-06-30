# Выход из цикла с помощью оператора break, если пользователь вводет значение 'quit'

prompt = "\nКакую начинку для пиццы вы хотите? "
prompt += "\nДля завершения программы нажмите 'quit': "

while True:

    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print(f"Мы добавили {topping} в вашу пиццу.")
