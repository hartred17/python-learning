current_users = ["eblan", "dima", "anton", "dyracho", "vladimir"]

new_users = ["eblan", "dyracho", "begemot", "danil", "pavel"]

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print("Данное имя занято. Выберите другое")
    else:
        print("Имя доступно")
