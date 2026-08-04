class Restaurant:
    """Ресторан."""

    def __init__(self, restaurant_name, cuisine_type):
        """Инициализирует атрибуты restaurant_name и cuisine_type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Выводит краткое описание ресторана."""
        msg = f"{self.restaurant_name} serves wounderful {self.cuisine_type}."
        print(f"\n{msg}")

    def open_restaurant(self):
        """Выводит сообщение о том, что ресторан открыт."""
        msg = f"{self.restaurant_name} is open. Come on in!"
        print(f"\n{msg}")


restaurant_1 = Restaurant("Ciniki", "salad")
restaurant_1.describe_restaurant()

restaurant_2 = Restaurant("McDonalds", "burger")
restaurant_2.describe_restaurant()

restaurant_3 = Restaurant("DodoPizza", "pizza")
restaurant_3.describe_restaurant()
