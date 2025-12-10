from os import abort

import mymodule
import math
name = input('введи свое имя: ')
print(mymodule.say_hello(name))
print(mymodule.ask_age())
print(mymodule.farewell(name))

mymodule.a = 19

# mymodule.aboba = 0

print(mymodule.a)

print(math.e)

print(math.pi)

# print(mymodule.aboba)
