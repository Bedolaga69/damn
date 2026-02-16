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

    def generate_loot(self, num_rolls=1):         #закинуть предметы(строки) с верояюностью потом роллить их потом закинуть в список и потом вернуть их
        loot_list = []
        for g in range(num_rolls):
            # ГЕНЕРАЦИЯ ЧИСЛА
            roll = random.random()
            # ОТСЛЕЖИВАНИЕ ВEРОЯТНОСТИ
            cumulative_probability = 0
            # ПРОХОД ПО ВСЕМ ПРЕДМЕТАМ
            for item_key, probability in self.loot_pool.items():
                cumulative_probability += probability
                if roll <= cumulative_probability:
                    if item_key in ITEMS:
                        loot_list.append(ITEMS[item_key])
                    break
        return loot_list


test = LootTable()
test.add_drop("heal_potion", 0.2)
test.add_drop("defense_potion", 0.3)
print(test.loot_pool)
print(test.generate_loot(3))
print(test.loot_pool)