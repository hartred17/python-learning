from pathlib import Path

name = input("Введите ваше имя: ")

path = Path('guest.txt')
path.write_text(name)