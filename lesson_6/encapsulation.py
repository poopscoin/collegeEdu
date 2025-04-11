class User:
    def __init__(self):
        self.__name = ""
        self.__email = ""
        self.__password = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_email(self, email):
        self.__email = email

    def get_email(self):
        return self.__email

    def set_password(self, password):
        self.__password = password

    def get_password(self):
        return self.__password

user = User()
user.set_name("Саша")
user.set_email("alex@gmail.com")
user.set_password("123456")

print(user.get_name())
print(user.get_email())
print(user.get_password())