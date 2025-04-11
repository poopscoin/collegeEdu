class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserManager:
    def __init__(self):
        self.__users = []

    def get_users(self):
        return self.__users

    def create_user(self, name, email):
        user = User(name, email)
        self.__users.append(user)
        return user

    def update_user(self, user, name=None, email=None):
        if name:
            user.name = name
        if email:
            user.email = email

    def delete_user(self, user):
        if user in self.__users:
            self.__users.remove(user)
            print(f"Користувача {user.name} видалено.")
        else:
            print("Користувача не знайдено.")
