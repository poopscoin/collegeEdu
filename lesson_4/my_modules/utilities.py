# 1. `calculate_average(numbers)`: Приймає список чисел `numbers` і повертає середнє арифметичне цих чисел.
# 2. `find_max(numbers)`: Приймає список чисел `numbers` і повертає найбільше число у списку.

numbers_history = []

def _add_in_history(numbers):
    if numbers not in numbers_history:
        numbers_history.append(numbers)

def calculate_average(numbers):
    _add_in_history(numbers)
    return sum(numbers) / len(numbers)

def find_max(numbers):
    _add_in_history(numbers)
    return max(numbers)