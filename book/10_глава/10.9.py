from pathlib import Path

file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    path = Path(file_name)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        pass
    else:
        print(f"\nСодержание файла {file_name}")
        print(f"\n{contents}")