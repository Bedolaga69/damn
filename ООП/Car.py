class Engine:
    def __init__(self, engine_type, power):
        self.engine_type = engine_type
        self.power = power
        self.is_running = False

    def start(self):
        if self.is_running is False:
            self.is_running = True
            print(f"Двигатель {self.engine_type} завелся! Мощность: {self.power} л.с.")
        else:
            print("Двигатель уже работает!")


class Wheels:
    def __init__(self, count, size):
        self.count = count
        self.size = size

    def get_wheel_info(self):
        return f"Колеса: {self.count} шт, размер: {self.size} дюймов"


class Car:
    def __init__(self, brand, model, engine_type, engine_power, wheel_count, wheel_size):
        self.brand = brand
        self.model = model
        self.engine = Engine(engine_type, engine_power)
        self.wheels = Wheels(wheel_count, wheel_size)

    def start(self):
        print(f"заводим {self.brand} {self.model}...")
        self.engine.start()

    def get_car_info(self):
        return f"{self.brand} {self.model} с {self.engine.engine_type} двигателем, {self.wheels.get_wheel_info()}"


# Пример использования
my_car = Car("BMW", "M6", "бензиновый", 560, 4, 21)

print(my_car.get_car_info())
my_car.start()