class Animal:  # базовый класс для всех животных класс это чертеж
    def __init__(self, name, species):  # конструктор принимает имя и вид
        self._name = name  # сохраняем имя животного
        self._species = species  # сохраняем вид животного

    def make_sound(self):  # метод-заглушка для звуков животных
        print("звук животного")  # базовое поведение

    def move(self):  # метод-заглушка для движения
        print(f"{self._name} двигается")  # базовое поведение

    def info(self):  # метод для печати информации о животном
        print(self._name)  # выводим имя


# --- ПТИЦЫ ---
class Bird(Animal):  # класс Bird наследует Animal
    def __init__(self, name):  # конструктор принимает только имя
        super().__init__(name, "Bird")  # вызываем конструктор Animal и указываем вид "Bird"
        # self.name = name # альтернативный вариант (не нужен, потому что super()._init_ уже сделал это)
        # Animal._init_(name)   # ещё один вариант вызова конструктора Animal (так тоже можно)


class Vorobei(Bird):  # воробей — наследник Bird
    def make_sound(self):  # переопределяем метод make_sound
        print("чирик")  # звук воробья

    def move(self):  # переопределяем метод move
        print("летает по небу")  # движение воробья


class Sinitsa(Bird):  # синица — наследник Bird
    def make_sound(self):  # переопределяем звук
        print("издает монгольское горловое пение")  # уникальный звук (шутка)

    def move(self):  # переопределяем движение
        print("n*gga MOVE!")  # (неподходящая фраза — лучше заменить)


# --- ДОМАШНИЕ ЖИВОТНЫЕ ---
class Mammals(Animal):  # млекопитающие наследуют Animal
    def __init__(self, name):  # конструктор принимает имя
        super().__init__(name, "Mammal")  # вызываем Animal и указываем вид "Mammal"


class Cat(Mammals):  # кошка — наследник Mammals
    def meow(self):
        print("мяу")  # звук кошки

    def move(self):
        print("бегает и играет")  # движение кошки


class Dog(Mammals):  # собака — наследник Mammals
    def bark(self):
        print("гав")  # звук собаки

    def move(self):
        print("бегает и виляет хвостом")  # движение собаки

def act(animal):#
    if isinstance(animal, Cat):
        animal.meow()
    elif isinstance(animal, Dog):
        animal.bark()

barsek = Cat("барсик")
bobik = Dog("бобик")

act(barsek)
act(bobik)

class Croco(Mammals):  # крокодил — наследник Mammals
    def make_sound(self):
        print("рыг")  # звук крокодила

    def move(self):
        print("плавает в озере")  # движение крокодила


class Giraffe(Mammals):  # жираф — наследник Mammals
    def make_sound(self):
        print("какой-то звук")  # звук жирафа

    def move(self):
        print("шагает на длинных ногах")  # движение жирафа


# animals = [  # список животных (закомментировано)
#     Vorobei("Воробей"),
#     Sinitsa("Синица"),
#     Cat("Барсик"),
#     Dog("Шарик"),
#     Croco("Крокодил"),
#     Giraffe("Жираф"),
# ]
#
# for a in animals:  # перебираем всех животных
#     print("----")  # разделитель
#     a.info()  # выводим имя
#     a.make_sound()  # каждый издаёт свой звук
#     a.move()  # и двигается по-своему
#
v = Vorobei("Вова")  # создаём объект класса Vorobei с именем «Вова»
print(v._name)  # печатаем имя воробья напрямую из атрибута