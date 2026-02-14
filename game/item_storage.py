from Items import *
import random


ITEMS = {
    "heal_potion": Consumable("зелье здоровья", "восстанавливает 30 здоровья", 95, "heal", 30),
    "attack_potion": Consumable("зелье урона", "дает +10 к урону", 150, "buff_attack", 10),
    "defense_potion": Consumable("зелье защиты", "дает +15 к защите", 100, "buff_defense", 15),
    "sword": Equipment("меч", "дает 33 урона", "weapon", 300, 33, 33),
    "bib": Equipment("броня", "дает 50 брони", "armor", 50, 250, 25)
}

# LOOT_TABLES = {
#     "Гоблин": [
#         {"item": "health_potion", "chance": 0.3, "min": 1, "max": 1},
#         {"item": "defense_potion", "chance": 0.3, "min": 1, "max": 1}
#     ],
#     "Орк": [
#         {"item": "health_potion", "chance": 0.5, "min": 1, "max": 1},
#         {"item": "sword", "chance": 0.1, "min": 1, "max": 1}
#     ],
#     "Скелет": [
#         {"item": "mana_potion", "chance": 0.7, "min": 1, "max": 1},
#         {"item": "bib", "chance": 0.1, "min": 1, "max": 1}
#     ]
# }

class LootTable:
    def __init__(self):
        self.loot_pool = {}

    def add_drop(self, item_key, probability):
        self.loot_pool[item_key] = probability

    def generate_loot(self):
        loot_list = []

        pass


test = LootTable()
test.add_drop("heal_potion", 0.2)
test.add_drop("defense_potion", 0.3)
print(test.loot_pool)
