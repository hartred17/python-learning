prompt = "\nКакую начинку для пиццы вы хотите? "
prompt += "\nДля завершения программы нажмите 'quit': "

topping = ""

while topping != "quit":
    topping = input(prompt)
    
    print(f"Мы добавили {topping} в вашу пиццу.")
