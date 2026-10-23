from pathlib import Path
import json

def get_stored_username(path):
    """Получает хранимое имя пользователя, если оно существует."""
    if path.exists():
            contents = path.read_text()
            username = json.loads(contents)
            return username
    else:
         return None


def get_new_username(path):
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username


def greet_user():
    """Приветствует пользователя по имени."""
    path = Path('username.json')
    username = get_stored_username(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username(path)

greet_user()