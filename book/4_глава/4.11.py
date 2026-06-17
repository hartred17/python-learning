pizzas = ["Margarita", "Diavola", "Peperoni"]

friend_pizzas = pizzas[:]

pizzas.append("Napolitana")

friend_pizzas.append("Shkolnya")

print("Мои любимые пиццы:")
for pizza in pizzas:
    print(f"- {pizza}")

print("\nЛюбимые пиццы моего друга:")
for friend_pizza in friend_pizzas:
    print(f"- {friend_pizza}")
