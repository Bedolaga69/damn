"""Сумма всех чисел: Напиши функцию sum_all,
которая принимает неограниченное количество числовых аргументов (используя *args) и возвращает их сумму."""
from dicttt.dict_hw import result

# def sum_all(*args):
#     return sum(args)
#
# print(sum_all(1,2,3,4,5,6,7,8,9,10))
#
#
# def sum_all(*args):
#     """можно и так"""
#     # Оставим только целые числа и числа с плавающей точкой
#     only_numbers = [n for n in args if isinstance(n, (int, float))]
#     return sum(only_numbers)
#
# print(sum_all(1, 2, "три", 4)) # Выведет 7, проигнорировав строку

"""Напиши функцию find_longest, которая принимает неограниченное количество строк
и возвращает самую длинную из них. Если передано несколько строк одинаковой (максимальной) длины, верни первую из них."""

# def find_longest(*args):
#     if not args:
#         return ""
#
#     return max(args, key=len)
#
# print(find_longest("кот","слон", "даун"))

"""Задача: «Пороговый сумматор»
Напиши функцию sum_greater_than, которая:

Первым аргументом принимает число limit (порог).

Затем принимает неограниченное количество чисел через *args.

Возвращает сумму только тех чисел из *args, которые строго больше значения

В определении функции limit должен стоять до *args.

Тебе понадобится цикл for для перебора чисел в args и переменная-счетчик (например, total = 0)."""

# def sum_greater_than(limit, *args):
#     total = 0
#     for n in args:
#         if n > limit:
#             total += n
#     return total
#
# print(sum_greater_than(10, 5, 20, 7, 15))

"""Напиши функцию describe_numbers, которая:

Принимает «метку» (строку, например "Результат").

Принимает неограниченное количество чисел (*args).

Возвращает строку, в которой написано: Метка + сумма чисел + максимальное число.

Здесь тебе нужно использовать и sum(args), и max(args).

Не забудь проверить, не пуст ли args, прежде чем искать максимум, иначе будет ошибка"""

# def describe_numbers(result, *args):
#     if not args:
#         return f"{result} данных нет"
#
#     return f"{result} сумма {sum(args)}, максимум {max(args)}"
#
# print(describe_numbers("отчет: ", 1, 5, 10))

"""Напиши функцию multi_filter(min_val, max_val, *args). 
Она должна вернуть список чисел из args, которые попадают в диапазон от min_val до max_val."""

def multi_filter(min_val, max_val, *args):
    return [n for n in args if n >= min_val and n <= max_val]
print(multi_filter(10, 20, 5, 12, 25, 17, 8))

# def multi_filter(min_val, max_val, *args):
#     """для примера как можно написать по другому"""
#     return [n for n in args if min_val <= n <= max_val]