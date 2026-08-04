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


class Admin(User):
    """Класс админ."""

    def __init__(self, first_name, last_name, username, email, location):
        """Инициализирую атрибуты класса родителя."""
        super().__init__(first_name, last_name, username, email, location)
        """Инициализирую пустой set привилегий."""
        self.privileges = Privileges()


class Privileges(Admin):
    """Привилегии."""

    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privileges(self):
        """Выводит привилегии."""
        print("\nPrivileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print(f"- У вас нет привелегий.")


ivan = Admin("ivan", "petrov", "pidr12", "pdr12@gmail.com", "moscow")
ivan.describe_user()
ivan.privileges.show_privileges()

ivan.privileges.privileges = [
    "разрешено добавлять сообщения",
    "разрешено удалять пользователей",
    "разрешено банить пользователей",
]

ivan.privileges.show_privileges()
