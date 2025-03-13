## **Завдання 1: Робота з функціями**
# Створіть Python-файл з ім'ям `calculator.py`. У цьому файлі створіть наступні функції:
# 1. `add(a, b)`: Приймає два числа `a` і `b` та повертає їхню суму.
# 2. `subtract(a, b)`: Приймає два числа `a` і `b` та повертає їхню різницю.
# 3. `multiply(a, b)`: Приймає два числа `a` і `b` та повертає їхній добуток.
# 4. `divide(a, b)`: Приймає два числа `a` і `b` і повертає результат ділення `a` на `b`. Пам'ятайте про можливість ділення на нуль і додайте перевірку цього варіанту.
# Після створення цих функцій, напишіть програму, яка імпортує модуль `calculator.py` і використовує його функції для виконання обчислень. Попросіть користувача ввести два числа і операцію (додавання, віднімання, множення або ділення), і виведіть результат обчислення.
## **Завдання 2: Створення та імпорт власних модулів**
# Створіть власний Python-модуль з ім'ям `utilities.py`. У цьому модулі створіть наступні функції:
# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.
# Після створення цього модуля, створіть інший Python-файл (наприклад, `main.py`), який імпортує модуль `utilities.py` і використовує його функції для обробки списку чисел.
# В `main.py` створіть список чисел та використовуйте функції з модуля `utilities` для знаходження середнього значення та найбільшого числа у списку. Виведіть результати на екран.

# Стандартні модулі
import random

# Мої модулі
from my_modules import calculator as canc_func
from my_modules import utilities as module

a = float(input("\nВведіть перше число: "))
b = float(input("Введіть друге число: "))
operation = str(input("Введіть операцію (-, +, *, /): "))

operations = {
    "+": canc_func.add,
    "-": canc_func.subtract,
    "*": canc_func.multiply,
    "/": canc_func.divide
}

if operation in operations:
    print(f"\n-> Результат: {operations[operation](a, b)}")
else:
    print("\n-> Невірна операція")

# =============================================================================
print("\n", "="*30, "\n")

def numbers_generate(count_min=4, count_max=10, min_num=10, max_num=100):
    numbers = []
    for i in range(random.randint(count_min, count_max)):
        numbers.append(random.randint(min_num, max_num))
    return numbers

numbers = numbers_generate()
print(f"-> Список чисел: {numbers}")

print(f"\n-> Середнє арифметичне: {module.calculate_average(numbers)}")

print(f"\n-> Найбільше число: {module.find_max(numbers)}")

numbers = numbers_generate()
print(f"\nОНОВЛЕННЯ -> Новий список чисел: {numbers}")

print(f"\n-> Середнє арифметичне: {module.calculate_average(numbers)}")

print(f"\n-> Найбільше число: {module.find_max(numbers)}")

print("\n", "="*30, "\n")

print(f"-> Історія списків чисел:")
for i, numbers in enumerate(module.numbers_history):
    print(f"{i+1}. - {numbers}")

print()