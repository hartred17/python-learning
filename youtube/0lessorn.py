def main():
    name = input("Введите имя ").strip().title()
    price = float(input("Введите цену заказа "))
    total = add_tax(price)
    print(f"Чек для {name}: ${total:.2f}")


def add_tax(p):
    return p * 1.05


main()
