class Car:
    def __init__(self, brand, model, year_of_release, color, speed = 0, is_started = False):
        self.brand = brand
        self.model = model
        self.year_of_release = year_of_release
        self.color = color
        self.speed = speed
        self.doors_locked = False
        self.is_started = is_started

    def start(self):
        self.is_started = True
        print("автомобиль заведен")

    def honk(self):
        if self.is_started:
            print("звук сигнала")
        else:
            print("автомобиль не заведен")

    def stop(self):
        self.is_started = False
        print("автомобиль заглушен")

    def speed_up(self, value):
        if self.is_started:
            self.speed += value
            print(f"скорость увеличена до:{self.speed}")
        else:
            print("машина не заведена")

    def slow_down(self, value):
        if self.is_started:
            self.speed = max(0, self.speed - value)
            print(f"скорость уменьшена до: {self.speed}")
        else:
            print("машина не заведена")

    def new_color_car(self, new_color):
        self.color = new_color
        print(f"перекрашен в {self.color}")

    def toggle_doors(self):
        self.doors_locked = not self.doors_locked
        if self.doors_locked:
            print("двери заблокированы")
        else:
            print("двери разблокированы")

    # def display_info(self):
    #     print(f"Марка: {self.brand}")
    #     print(f"Модель: {self.model}")
    #     print(f"Год выпуска: {self.year_of_release}")
    #     print(f"Цвет: {self.color}")
    #     print(f"текущая скорость:{self.speed}")

    def __str__(self):
        return (f"Марка:{self.brand}\nМодель: {self.model}\nГод выпуска: {self.year_of_release}\n"
                f"Цвет: {self.color}\nТекущая скорость:{self.speed}")

my_car = Car("Mersedes", "w222", 2014, "black")
print(my_car)
# my_car.display_info()
my_car.start()
my_car.toggle_doors()
my_car.honk()
my_car.speed_up(120)
my_car.slow_down(40)
my_car.slow_down(1000000)
my_car.stop()
my_car.new_color_car("фиолетовый")
