class Inventory:
    # def __init__(self):
    #     self.products = {}
    def __init__(self, products=None, **kwargs):
        if products is None:
            products = {}
        if products:
            self.products = products
        else:
            self.products = kwargs

    def add_product(self, name, quantity=1):
        if name in self.products:
            self.products[name] += quantity
        else:
            self.products[name] = quantity
        print(f"добавленно {name} - {quantity} штук")


    def remove_product(self, name, quantity=1):
        if name not in self.products:
            print(f"ошибка {name} нет на складе")

        if self.products[name] < quantity:
            print(f"ошибка, недостаточно {name}")
            return False

        self.products[name] -= quantity
        print(f"убрано {name} - {quantity} штук")

        if self.products[name] == 0:
            del self.products[name]
        return True

    def check_availability(self, name):
        if name in self.products:
            print(f"{name} есть {self.products[name]} штук")
        else:
            print(f"{name} нет в наличии")

    def get_quantity(self, name):
        quantity = self.products.get(name, 0)
        print(f"{name}: {quantity} штук")
        return quantity

    def show_all_products(self):
        print("---товары на складе---")
        for product, quantity in self.products.items():
            print(f"{product}: {quantity} штук")
        if not self.products:
            print("склад пуст")

# пример использования
warehouse = Inventory()# создание блокнота
# добавляем товары
warehouse.add_product("яблоки", 10)# записываем товары
warehouse.add_product("бананы", 5)
warehouse.add_product("яблоки", 3)
# проверяем наличие
warehouse.check_availability("яблоки")# проверка на наличие
warehouse.check_availability("апельсины")
# убираем товары
warehouse.remove_product("бананы", 2)# удаление товара
warehouse.remove_product("бананы", 10)
# показываем все продукты
warehouse.show_all_products()# вывод того что осталось
