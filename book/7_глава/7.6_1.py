# Завершение цикла при проверке условия в операторе while

prompt = "\nКакую начинку для пиццы вы хотите? "
prompt += "\nДля завершения программы нажмите 'quit': "

topping = ""

while topping != "quit":
    topping = input(prompt)
    
    if topping != 'quit':
        print(f"Мы добавили {topping} в вашу пиццу.")
