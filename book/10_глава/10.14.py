from pathlib import Path
import json

def get_stored_username(path):
    """Получает хранимое имя пользователя, если оно существует."""
    if path.exists():
            contents = path.read_text()
            user_data = json.loads(contents)
            return user_data
    else:
         return None


def get_new_username(path):
    """Запрашивает новое имя пользователя."""
    username = input("What is your name? ")
    age = input("How old are you? ")
    nickname = input("Enter your nickname: ")
    user_data = {'username': username, 'age': age, 'nickname': nickname}
    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data


def greet_user():
    """Приветствует пользователя по имени."""
    path = Path('username.json')
    user_data  = get_stored_username(path)

    if user_data:
        answer = input(f"Are you {user_data['username']}?(y/n)")
        if answer == 'y':
            print(f"Welcome back, {user_data['username']}!")
            print(f"Your nickname is {user_data['nickname']}")
            print(f"Your age is {user_data['age']}")
        else:
            user_data = get_new_username(path)
            print(f"We'll remember you when you come back, {user_data['username']}!")  
    else:
        user_data = get_new_username(path)
        print(f"We'll remember you when you come back, {user_data['username']}!")

greet_user()