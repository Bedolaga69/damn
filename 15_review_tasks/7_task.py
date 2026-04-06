"""Частота символов: Напиши функцию, которая считает, сколько раз каждый символ встречается в строке "hello world"""

# def search_word(string):
#     processed = []
#     for char in string:
#         if char not in processed:
#             print(char, string.count(char))
#             processed.append(char)
#
# text = "hello world"
# search_word(text)

"""Напиши функцию, которая принимает строку и делает следующее:

Считает, сколько раз в этой строке встречаются только гласные буквы (а, е, ё, и, о, у, ы, э, ю, я — для русского или a, e, i, o, u — для английского).

Выводит результат в формате: Буква "а" встретилась 3 раз(а).

Условие: Если гласная буква ни разу не встретилась в строке, её выводить не нужно.

Важно: Используй тот же подход через список processed и цикл for, который мы разобрали выше, но добавь проверку: является ли текущий символ гласной буквой."""

# def search_letter(string):
#     vowels = "aeiouаеёиоуыэюя"
#     already_counted = []
#     for char in string.lower():
#         if char.lower() in vowels and char not in already_counted:
#             already_counted.append(char)
#             print(f" буква: {char}, встречается: {string.lower().count(char)} раз")
#
# text = "hello world, привет мир"
# search_letter(text)

"""Напиши функцию, которая принимает список слов и печатает только те, в которых больше 5 букв"""

# def boba(words):
#     for word in words:
#         if len(word) > 5:
#             # word = word[:5]
#             print(word)
#
# text = ["яблоко", "банан", "дом", "машина"]
# boba(text)


"""Напиши функцию, которая принимает список чисел (и положительных, и отрицательных) и считает сумму только положительных чисел"""
# def hello_world(numbers):
#     total_sum = 0
#     for number in numbers:
#         if number >= 0:
#             total_sum = number + total_sum
#     print(total_sum)
#
# num = [12, 43, -1, 0, 15, -67]
# hello_world(num)

"""Напиши функцию, которая проверяет, подходит ли пароль под требования безопасности.
Пароль считается хорошим, если в нем есть хотя бы одна цифра и он длиннее 8 символов"""

def check_password(password):
    fits = False
    if len(password) < 8:
        print("пароль короткий")
    else:
        # fits = any(num.isdigit() for num in password)
        for num in password:
            if num.isdigit():
                fits = True
                break
        if fits:
            print("все нормик")
        else:
            print("длина норм но не хватает цифр")


fsdf = input("введите парол: ")
check_password(fsdf)
