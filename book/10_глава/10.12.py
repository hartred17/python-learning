from pathlib import Path
import json

path = Path('favourite_number.json')
try:
    contents = path.read_text()
except FileNotFoundError:
    print("Какое ваше любимое число ?")
    favourite_number = int(input())
    contents = json.dumps(favourite_number)
    path.write_text(contents)
    print("Спасибо, я запомню его.")
else:
    favourite_number = json.loads(contents)
    print(f"Я знаю ваше любимое число! Это {favourite_number}")