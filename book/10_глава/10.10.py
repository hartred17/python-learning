from pathlib import Path

path = Path('Dead_Souls_Gogol.txt')

try:
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Файл {path} не найден.")
else:
    count = contents.lower().count('the ')
    print(f"Артикль 'The' встречается в тексте {path} {count} раз.")