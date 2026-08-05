from user import User
from privileges import Admin, Privileges

admin = Admin('anton', 'novikov', 'anton1o', 'anton12@gmail.com', 'moscow')
admin.privileges.privileges = [
    "разрешено добавлять сообщения",
    "разрешено удалять пользователей",
    "разрешено банить пользователей",
]

admin.describe_user()
admin.privileges.show_privileges()