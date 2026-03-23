"""Генератор списков: Создай список из квадратов всех нечетных чисел в диапазоне от 1 до 15,
используя list comprehension."""
squares = [x ** 2 for x in range(1, 16) if x % 2 != 0]
print(squares)
#task complete