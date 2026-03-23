"""FizzBuzz: Напиши функцию, которая выводит числа от 1 до 20. Если число делится на 3,
выведи "Fizz", если на 5 — "Buzz", если на оба — "FizzBuzz", иначе — само число."""

def fizz_buzz():
    num = int(input("введите число от 1 до 20: "))
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 5 == 0:
            print("Buzz")
    elif num % 3 == 0:
            print("Fizz")
    else:
        print(num)

fizz_buzz()

#task complete