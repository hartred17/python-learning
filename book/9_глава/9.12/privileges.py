from user import User


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