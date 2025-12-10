# x1, y1, x2, y2 = map(int, input().split())
#
# Ввод пользователя: 4 4 5 5
# Что происходит:
# input() → "4 4 5 5"
# .split() → ['4', '4', '5', '5']
# map(int, ...) → числа 4, 4, 5, 5
# Присваивание:
# x1 = 4
# y1 = 4
# x2 = 5
# y2 = 5


# abs()
# Функция abs() в Python — это встроенная функция,
# которая возвращает абсолютное значение (модуль) числа.
# То есть она превращает отрицательное число в положительное,
# а положительное оставляет без изменений.


#  Зачем abs() в задаче про шахматного короля?
# В коде:
# python
# if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
#     print("YES")
# else:
#     print("NO")
# Мы проверяем, что:
# Разница между x1 и x2 ≤ 1 (по горизонтали)
# Разница между y1 и y2 ≤ 1 (по вертикали)
# Но если x1 < x2, то x1 - x2 даст отрицательное число. Чтобы не учитывать знак, мы берём модуль (abs).
# Пример:
# Король стоит на (4, 4), хочет пойти на (5, 5).
# x1 - x2 = 4 - 5 = -1 → abs(-1) = 1 (подходит)
# y1 - y2 = 4 - 5 = -1 → abs(-1) = 1 (подходит)
# Вывод: YES (может пойти)
# Король на (1, 1), хочет пойти на (3, 2).
# x1 - x2 = 1 - 3 = -2 → abs(-2) = 2 (слишком далеко → NO)
# y1 - y2 = 1 - 2 = -1 → abs(-1) = 1 (но по x уже не подходит)
# Вывод: NO (не может пойти)


# параметры print end и sep=

# f2 = open(file="bleh/amogus.txt", mode='w')
# f3 = open(mode='w', file="bleh/amogus.txt")
#
# f2.write("amogus\naboba")
# f2.close()
#



# text = "12".isdigit()
# print(text)
# isdigit метод строк
# когда есть is оно возвращает обычно булевое значение


# print(isinstance(12, int)) #она проверяет является ли объект экземпляром указанного класса и возвращает True или False



# isinstance(object, type)#


class Person:

    def __init__(self, name):
        self.__name = name  # имя человека

    @property
    def name(self):
        return self.__name

    def do_nothing(self):
        print(f"{self.name} does nothing")


#  класс работника
class Employee(Person):

    def work(self):
        print(f"{self.name} works")


#  класс студента
class Student(Person):

    def study(self):
        print(f"{self.name} studies")


def act(person):
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Employee):
        person.work()
    elif isinstance(person, Person):
        person.do_nothing()


tom = Employee("Tom")
bob = Student("Bob")
sam = Person("Sam")

act(tom)
act(bob)
act(sam)