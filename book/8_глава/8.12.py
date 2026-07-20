def make_sandwich(*toppings):
    """Выводит список компонентов бутерброда."""
    print(f"\nДелаем бутерброд с следующими начинками:")
    for topping in toppings:
        print(f"- {topping}")

make_sandwich('cheese')
make_sandwich('shese', 'onion')
make_sandwich('mushrooms', 'meat', 'cucumber')
