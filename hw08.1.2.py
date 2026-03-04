import re
from typing import Callable




# ЗАВДАННЯ1
def caching_fibonacci():
    # Створюємо словник для кешування обчислених чисел Фібоначчі
    cache = {}

    def fibonacci(n):
        """Рекурсивна функція для обчислення n-го числа Фібоначчі з кешуванням."""
        if n <= 0:
            return 0
        if n == 1:
            return 1

        # Перевіряємо, чи результат уже в кеші
        if n in cache:
            return cache[n]

        # Якщо немає в кеші, обчислюємо рекурсивно
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # Повертаємо внутрішню функцію (замикання), яка зберігає cache
    return fibonacci

# Отримуємо функцію fibonacci з кешем
fib = caching_fibonacci()

print(fib(10))  # 55
print(fib(15))  # 610
print(fib(20))  # 6765




# ЗАВДАННЯ 2
def generator_numbers(text: str):
    """
    Генератор дійсних чисел у тексті.
    Використовує регулярний вираз для пошуку чисел, відокремлених пробілами.
    """
    # Регулярний вираз для дійсних чисел (цілі + дробові)
    pattern = r'(?<=\s)\d+\.\d+|\d+(?=\s)'
    for match in re.finditer(pattern, text):
        yield float(match.group())

def sum_profit(text: str, func: Callable):
    """
    Підсумовує всі дійсні числа, які повертає генератор func(text).
    """
    return sum(func(text))

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")



