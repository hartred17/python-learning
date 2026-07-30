class Restaurant:
    """Ресторан."""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты restaurant_name и cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Выводит краткое описание ресторана."""
        msg = f"{self.restaurant_name} serves wounderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт."""
        msg = f"{self.restaurant_name} is open. Come on in!"
        print(f"\n{msg}")

    def set_number_served(self, number):
        """Задает количество обслуженных посетителей."""
        self.number_served = number

    def increment_number_served(self, amount):
        """Увеличивает количество обслуженных посетителей на заданную величину."""
        self.number_served += amount

class IceCreamStand(Restaurant):
    """Киоск с мороженным."""

    def __init__(self, restaurant_name, cuisine_type='ice cream'):
        """Инициализирует атрибуты класса родителя."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = []

    def show_flavours(self):
        """Выводит список flavours."""
        print("\nWe have the following flavors available: ")
        for flavour in self.flavours:
            print(f"- {flavour.title()}")


ice_cream = IceCreamStand('Ice Paradice')
ice_cream.flavours = ['vannila', 'chocolate', 'strawberry']

ice_cream.describe_restaurant()
ice_cream.show_flavours()
