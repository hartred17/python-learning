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


restaurant = Restaurant("Ciniki", "pizza")
restaurant.describe_restaurant()

print(f"\nNumber served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(15)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(50)
print(f"Number served: {restaurant.number_served}")
