def say_hello(name):
    print(f"привет, {name}")

def ask_age():
    age = input("сколько тебе лет? ")
    print("а ты взрослый")

def farewell(name):
    print(f"прощай, {name}!")

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        print("на ноль нельзя делить")
        return 0
    else:
        return a / b

def addition(a, b):
    return a + b

