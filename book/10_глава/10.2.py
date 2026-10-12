from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text()

modified_contents = contents.replace('Python', 'C')
print(modified_contents)