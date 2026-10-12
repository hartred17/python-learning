from pathlib import Path

names = ""

while True:
    name = input("Введите ваше имя (или q для выхода): ")
    if name.lower() == "q":
        break
    
    print(f"Привет, {name.title()}.")
    names += f"Привет, {name.title()}.\n"

path = Path('guest_book.txt')
path.write_text(names)