prompt = "\nКакую начинку для пиццы вы хотите? "
prompt += "\nДля завершения программы нажмите 'quit': "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print(f"Мы добавили {topping} в вашу пиццу.")
    else:
        break
