"""Класс «Автомобиль»: Создай класс Car с атрибутами brand и year.
Добавь метод get_info, который выводит строку: "Марка: [brand], Год: [year]"."""

class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def get_info(self):
        return f"Марка: {self.brand}, Год: {self.year}"

my_car = Car("мерседес", 2020)
print(my_car.get_info())