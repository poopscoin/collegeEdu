### Цикли:
# 1. **Таблиця множення:**
#    Завдання: Виведіть таблицю множення для заданого числа від 1 до 10.
# 2. **Сума чисел:**
#    Завдання: Визначте список чисел і обчисліть їх суму.
# 3. **Факторіал числа:**
#    Завдання: Обчисліть факторіал заданого числа.
# 4. **Парні числа:**
#    Завдання: Виведіть всі парні числа від 1 до 50.
# 5. **Пошук простих чисел:**
#    Завдання: Знайдіть всі прості числа в заданому діапазоні.
import random

# 1. **Таблиця множення:**
number = int(input("1 Завдання\n\nВведіть число: "))
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")

# 2. **Сума чисел:**
numbers = []
for _ in range(random.randint(4, 18)):
    numbers.append(random.randint(1, 100))
print(f"\n2 Завдання\n\nЗгенерований список чисел: {numbers}")
sum_numbers = 0
for number in numbers:
    sum_numbers += number
print(f"Сума чисел: {sum_numbers}")

# 3. **Факторіал числа:**
number = int(input("\n3 Завдання\n\nВведіть число: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"Факторіал числа {number} дорівнює {factorial}")

# 4. **Парні числа:**
print("\n4 Завдання\n\nПарні числа від 1 до 50:")
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=" ")
print()

# 5. **Пошук простих чисел:**
start = random.randint(1, 50)
end = random.randint(start, 100)
print(f"\n5 Завдання\n\nПочаток діапазону: {start}")
print(f"Кінець діапазону: {end}")
print(f"\nПрості числа в діапазоні від {start} до {end}:")
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
print('\n')
