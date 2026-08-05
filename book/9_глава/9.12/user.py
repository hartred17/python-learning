class User:

    def __init__(self, first_name, last_name, username, email, location):
        """Инициализирует атрибуты first_name и last_name."""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.username = username
        self.email = email
        self.location = location.title()
        self.login_attems = 0

    def describe_user(self):
        """Выводит сводку с информацией о пользователе."""
        print(f"\n{self.first_name} {self.last_name}")
        print(f"    Имя пользователя: {self.username}")
        print(f"    Email: {self.email}")
        print(f"    Место жительства: {self.location}")

    def greet_user(self):
        """Выводит персональное приветсвие для пользователя."""
        print(f"\nДобрый день, {self.username}")

    def increment_login_attempt(self):
        """Увеличивает значение login_attems на 1."""
        self.login_attems += 1

    def reset_login_attemps(self):
        """Обнуляет значение login_attems."""
        self.login_attems = 0