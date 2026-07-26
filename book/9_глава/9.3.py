class User:

    def __init__(self, first_name, last_name, username, email, location):
        """Инициализирует атрибуты first_name и last_name."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()

    def describe_user(self):
        """Выводит сводку с информацией о пользователе."""
        print(f"{self.first_name} {self.last_name}")
        print(f"Имя пользователя: {self.username}")
        print(f"Email: {self.email}")
        print(f"Место жительства: {self.location}")

    def greet_user(self):
        """Выводит персональное приветсвие для пользователя."""
        print(f"Добрый день {self.username}")

user_1 = User('anton', 'karpov', 'antonch1k', 'antonch1k@gmail.com', 'astana')
user_2 =