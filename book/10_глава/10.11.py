from pathlib import Path
import json

print("Какое ваше любимое число ?")
favourite_number = int(input())

path = Path('favourite_number.json')
contents = json.dumps(favourite_number)
path.write_text(contents)