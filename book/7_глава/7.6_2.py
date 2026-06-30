# Управление продолжительностью выполнения цикла в зависимости от переменной active

prompt = "\nКакую начинку для пиццы вы хотите? "
prompt += "\nДля завершения программы нажмите 'quit': "

active = True

while active:
    topping = input(prompt)

    if topping == 'quit':
        active = False
    else:
        print(f"Мы добавили {topping} в вашу пиццу.")