def say_hello(name):
    """функция здоровается"""
    print(f"hello, {name}!")

say_hello("вова")
say_hello("алексе")

def max(a, b):
    """функция сравнивает два числа: a и b"""
    if a>b:
        return a
    else:
        return b

max(4, 5)