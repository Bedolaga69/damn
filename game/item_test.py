from dataclasses import dataclass
@dataclass
class Item:
    name: str
    description: str
    item_type: str
    value: int
    stackable: bool = True
    quantity: int = 1

@dataclass
class Consumable(Item):
    effect_type: str
    effect_value: int

class Equipment(Item):
    def __init__(self, name, description, item_type, value, quantity, stat_boost, bonus_damage):
        super().__init__(name, description, item_type, value, quantity, stat_boost, bonus_damage)
        self.stat_boost = {}
        self.bonus_damage = bonus_damage
