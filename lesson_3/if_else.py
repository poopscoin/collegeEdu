### Умовні конструкції:
# 1. **Перевірка паролю:**
#    Завдання: Напишіть програму, яка встановлює початковий пароль і перевіряє, чи введений користувачем пароль співпадає з ним. Якщо пароль дорівнює "password123", виведіть повідомлення "Ви увійшли в систему". В іншому випадку виведіть повідомлення "Неправильний пароль".
# 2. **Визначення днів тижня:**
#    Завдання: Створіть програму, яка встановлює номер дня тижня і виводить назву відповідного дня тижня. Якщо номер дня недійсний (менше 1 або більше 7), виведіть повідомлення про помилку.

# 1. **Перевірка паролю:**
data = [
    {
        "login": "admin",
        "password": "password123"
    },
    {
        "login": "user",
        "password": "topsecret"
    }
]

user_login = input("\nВведіть логін: ")

login_index = -1
for index, user in enumerate(data):
    if user["login"] == user_login:
        login_index = index
        break

if login_index != -1:
    user_password = input("\nВведіть пароль: ")
    if data[login_index]["password"] == user_password:
        print("\nВи увійшли в систему\n")
    else:
        print("\nНеправильний пароль\n")
else:
    print("\nТакого користувача не існує.\n")

# 2. **Визначення днів тижня:**
week_days = ["Понеділок", "Вівторок", "Середа", "Четвер", "Пʼятниця", "Субота", "Неділя"]

day_number = int(input("2 Завдання\n\nВведіть номер дня тижня: "))
if 0 < day_number < 8:
    print(f"\n{week_days[day_number - 1]}\n")
else:
    print("\nНеправильний номер дня тижня\n")