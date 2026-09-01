from pathlib import Path

print("--- Чтение всего файла:")
path = Path('learning_python.txt')
contents = path.read_text()
print(contents)

print("\n--- Разбиение текста на отдельные строки:")
lines = contents.splitlines()
for line in lines:
    print(line) 
