class Item:
    def __init__(self, name, description, item_type, value, stackable = True, quantity = 1):
        self.name = name
        self.description = description
        self.item_type = item_type
        self.value = value
        self.stackable = stackable
        self.quantity = quantity

class Consumable(Item):
    def __init__(self, name, description, item_type, value, effect_type, effect_value):
        super().__init__(name, description, item_type, value)
        self.effect_type = effect_type
        self.effect_value = effect_value
    def __str__(self):
        return (f"{self.name}, {self.description}, {self.item_type}, {self.value}, {self.effect_value},"
                f" {self.effect_type}, {self.stackable}, {self.quantity}")

potion = Consumable("фласка", "восстанавливает 30 здоровья", "зелье восстановления",
                    95, "лечение", 40)
print(potion)