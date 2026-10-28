from pathlib import Path
import json

path = Path('favourite_number.json')
contents = path.read_text()
favourite_number = json.loads(contents)

print(f"Я знаю ваше любимое число! Это {favourite_number}")