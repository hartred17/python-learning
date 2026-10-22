from pathlib import Path

file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    print(f"\nСодержание файла {file_name}")
    path = Path(file_name)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"\nФайл {file_name} не найден.")
    else:
        print(f"\n{contents}")