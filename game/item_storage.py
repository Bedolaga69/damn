from Items import *
import random


ITEMS = {
    "heal_potion": Consumable("зелье здоровья", "восстанавливает 30 здоровья", 95, "heal", 30),
    "attack_potion": Consumable("зелье урона", "дает +10 к урону", 150, "buff_attack", 10),
    "defense_potion": Consumable("зелье защиты", "дает +15 к защите", 100, "buff_defense", 15),
    "sword": Equipment("меч", "дает 33 урона", "weapon", 300, 33, 33),
    "armor": Equipment("броня", "дает 50 брони", "armor", 50, 250, 25)
}


class LootTable:
    def __init__(self):
        self.loot_pool = {}

    def add_drop(self, item_key, probability):
        self.loot_pool[item_key] = probability

    def generate_loot(self, num_rolls=1):
        loot_list = []
        for item_key, probability in self.loot_pool.items():
            roll = random.random()
            cumulative_probability = 0
            for g in range(num_rolls):
                cumulative_probability += probability
                if roll <= cumulative_probability:
                    if item_key in ITEMS:
                        loot_list.append(ITEMS[item_key])
                    break
        return loot_list


test = LootTable()
test.add_drop("heal_potion", 0.4)
test.add_drop("defense_potion", 0.3)
test.add_drop("sword", 0.1)
test.add_drop("armor", 0.08)
# print(test.loot_pool)
# print(test.generate_loot())
# print(test.loot_pool)
print(test.generate_loot(3))
# print(test.loot_pool)

