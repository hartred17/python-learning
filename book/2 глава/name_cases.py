#2.3
name = "Еблан"
print(f"Здравствуйте, {name}, не хотите ли вы изучит Python сегодня?")

user = "василий лошков"
#2.4
print(user.lower())
print(user.upper())
print(user.title())

#2.5
print('Фридрих Ницше говорил: "Всё, что нас не убивает, делает нас сильнее.”')

#2.6
famous_person = "Фридрих Ницше"
message = f'{famous_person} говорил: "Всё, что нас не убивает, делает нас сильнее.”'
print(message)

#2.7
user_name = "  \tПетр\n  "
print(user_name)
print(user_name.lstrip())
print(user_name.rstrip())
print(user_name.strip())

#2.8

filename = 'python_notes.txt'
print(filename.removesuffix('.txt'))
