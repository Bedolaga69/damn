# ZeroDivisionError

# a = 0
# if a != 0:
#     print(5/a)
# else:
#     print("нельзя делить на ноль")

# try:
#     k = 5/a
# except ZeroDivisionError:
#     print("Zero Division")

# BaseException базовое исключение от которого берут начало все остальные
# напрямую не используют
# KeyboardInterrupt порождается при прерывании программы пользователя ctrl + f2
#
# IndexError индекс не выходит в диапазон элементов
# l = 1, 2, 3, 4, 5
# print(type(l))
# for i in range(len(l)+1):
#     print(l[i])

# NameError не найдено переменной с таким именем
# if aboba > 5:
#     print("aboba")

# TypeError операция применена к объекту
# 5 + "hello"
# "hello" + 5 # присоединение строк конкатинация


# ValueError функция получает аргумент правильного типа но некорректного значения
# int(input())

# num_str = input("введите число: ")
# if num_str.isdigit():
#     num = int(num_str)
# else:
#     print("введено не число!")

# s_test = "20 432 54 67 45"
# l = s_test.split()
# print(l)

# print(s_test.count("5"))

# s_test = "hello"
# print(s_test.islower())

# try:
#     num = int(input("введите число: "))
# except ValueError:
#     print("введено не число!")

# FileNotFoundError появляется тогда когда программа пытается открыть несуществующий файл
#
# try:
#     with open("несуществующий_файл.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError as e:
#     print(f"Ошибка! Файл не найден: {e}")

# with open(...) as file: менеджер контекста для работы с файлами
# "r"  режим чтения (read)
# as file файловый объект, с которым будем работать
# content  file.read() - чтение всего содержимого файла
# except FileNotFoundError - ловит конкретно это исключение
# as e сохраняет объект в переменную e
#
# KeyError ошибка возникает при попытке доступа к несуществующему ключу в словаре
# my_dict = {'name': 'Alice', 'age': 25}
# try:
#     print(my_dict['address'])
# except KeyError:
#     print("ошибка")


# BaseException это базовый класс всех (обрабатываемых) исключений в Python. От него наследуются все остальные исключения, включая Exception.
#
# Exception это базовый класс обычных (обрабатываемых) исключений. От него наследуются такие исключения, как ValueError, TypeError и т.д.
#
# while True:
#     try:
#         num_input = int(input("введите число: "))
#     except ValueError:
#         print("ошибка, вы ввели не число")
#     else:
#         break
#     finally:
#         print("спасибо за ввод!")

# FileNotFoundError
# try:
#     with open("non_existing_file.txt", "r") as file:
#         content = file.read()
# except FileNotFoundError:
#     print("файл не найден")

# FileExistsError
# with open("example.txt", "x") as f:
#     f.write("hello world")

# with open("example.txt", "x") as f:
#     f.write("error")

# ModuleNotFoundError
# AttributeError