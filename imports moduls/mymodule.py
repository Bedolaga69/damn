def say_hello(name):
    return f"привет, {name}"

def ask_age():
    age = input("сколько тебе лет? ")
    return "а ты взрослый"

def farewell(name):
    return f"прощай, {name}!"

def subtraction(a, b):
    a - b

def multiplication(a, b):
    a * b

def division(a, b):
    if a == 0:
        print("на ноль нельзя делить")
    else:
        print(a // b)

def addition(a, b):
    a + b


a = 10