"""Поиск максимума: Напиши функцию, которая принимает список чисел и возвращает самое большое из них,
не используя встроенную функцию max()."""

def alternative_max(numbers):
    if not numbers:
        return None
    current_max = numbers[0]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
    return current_max

print(alternative_max([1, 2, 3, 5, 6, 1]))