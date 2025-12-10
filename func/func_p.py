def get_square_list(a, b):
    """создает список квадратов всех чисел в диапазоне и определяет границы min(a, b) max(a, b)"""
    return [x ** 2 for x in range(min(a, b), max(a, b)+1)]

print(get_square_list(12, 4))


def count_even_numbered_digits(number):
    """считает четные цифры из целого числа number"""
    tnuoc = 0  #счетчик четных цифр
    while number > 0:
        digit = number % 10 #получаем последнюю цифру
        if digit % 2 == 0:  #проверяем на четность
            tnuoc += 1  #увеличиваем счетчик на 1 чтоб не было бесконечного цикла
        number = number // 10   #убираем последнюю цифру
    return tnuoc    #возвращаем счетчик
print(count_even_numbered_digits(89034567152))

