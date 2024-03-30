class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def get_user_id(self):
        return self._user_id

    def get_name(self):
        return self._name

    def get_access_level(self):
        return self._access_level


class Admin(User):
    def __init__(self, user_id, name, access_level='admin'):
        super().__init__(user_id, name, access_level)
        self._users = []

    def add_user(self, user):
        self._users.append(user)

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)

    def list_users(self):
        return self._users

    def get_admin_name(self):
        return self.get_name()

# ТЕСТ

user1 = User(1, "Маша")
user2 = User(2, "Саша")
user3 = User(3, "Даша")
admin = Admin(3, "Игорь Валерьевич")

admin.add_user(user1)
admin.add_user(user2)
admin.add_user(user3)

print("Администратор:", admin.get_admin_name())

print("\nСписок пользователей в системе:")
for user in admin.list_users():
    print(user.get_name())

admin.remove_user(user2)

print("\nОбновленный список пользователей в системе:")
for user in admin.list_users():
    print(user.get_name())
