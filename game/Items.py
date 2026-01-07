class Item:
    """главный класс от которого и наследуются следующие классы"""
    def __init__(self, name, description, value,effect_value, stackable = True, quantity = 1, ):
        self.name = name
        self.description = description
        self.value = value
        self.stackable = stackable
        self.quantity = quantity
        self.effect_value = effect_value

    def __eq__(self, other):
        return other.name == self.name

    def __hash__(self):
        return hash(self.name)

class Consumable(Item):
    """класс расходников (наследуется от класса Item)
    name - имя
    description - описание
    item_type - тип предмета
    value цена - предмета
    effect_type - тип эффекта
    effect_value - величина эффекта
    """
    def __init__(self, name, description, value, effect_type, effect_value):
        super().__init__(name, description, value, effect_value)
        self.effect_type = effect_type
    def __str__(self):
        return (f"{self.name}, {self.description}, {self.value}, {self.effect_value},"
                f" {self.effect_type}, {self.stackable}, {self.quantity}")

    def __eq__(self, other):
        return other.name == self.name

    def __hash__(self):
        return hash(self.name)


class Equipment(Item):
    """класс снаряжения
    durability_value - кол-во едениц снаряжения
    equipment_type - тип желаемого снаряжения(шлем, нагрудник, поножи, обувь)"""
    def __init__(self, name, description, equipment_type, value, effect_value, durability_value):
        super().__init__(name, description, value, effect_value)
        self.durability_value = durability_value
        self.equipment_type = equipment_type

    def __repr__(self):
        return f"<{self.name} ({self.effect_value})>"

    def __str__(self):
        return f"{self.name}, {self.description}, {self.value}, {self.durability_value}"

    def __eq__(self, other):
        return other.name == self.name

    def __hash__(self):
        return hash(self.name)


armor = Equipment("броня", "дает 50 брони", "нагрудник", 250, 50, 25)
potion = Consumable("фласка", "восстанавливает 30 здоровья",95, "лечение", 40)
"""вывод в консоль информации о чем либо(сейчас об снаряжении и зелье)"""
# print(armour)
# print(potion)