usernames = []

if usernames:
    for name in usernames:
        if name == "admin":
            print(f"Здравствуйте, {name}, хотите посмотреть отчет о состоянии дел ?")
        else:
            print(f"Привет, {name}, спасибо, что авторизовался в системе ")
else:
    print("Нам нужно добавить несколько пользователей!")
