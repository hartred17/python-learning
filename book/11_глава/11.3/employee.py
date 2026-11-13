class Employee:
    """Представляет работника."""

    def __init__(self, first_name, last_name, salary):
        """Определяет имя, фамилию, годовую зарплату."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.sallary = salary

    def give_raise(self, amount=5000):
        """Увеличивает оклад на 5000 долларов по умолчанию, может получать другую сумму."""
        self.sallary += amount

