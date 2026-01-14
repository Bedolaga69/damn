import random
from game_units import *

class Warrior(Unit):
    def __init__(self, name, health, attack, defense, equipped_weapon=None, equipped_armor=None):
        super().__init__(name, health, attack, defense)
        self.inventory = []
        self.equipped_weapon = equipped_weapon
        self.equipped_armor = equipped_armor
        self.base_defense = defense
        self.base_attack = attack
        self.defense = self.base_defense
        if self.equipped_armor:
            self.defense += self.equipped_armor.effect_value
        self.attack = self.base_attack
        if self.equipped_weapon:
            self.attack += self.equipped_weapon.effect_value

    def use_item(self, item):
        if isinstance(item, Equipment):
            if item in self.inventory:
                if item.equipment_type == "weapon":
                    if self.equipped_weapon is not None:
                        old_weapon = self.equipped_weapon
                        self.attack -= old_weapon.effect_value
                        self.inventory.append(old_weapon)
                    self.equipped_weapon = item
                    self.attack += item.effect_value
                    self.inventory.remove(item)
                    print(f"вы экипировали {item.name}")
                elif item.equipment_type == "armor":
                    if self.equipped_armor is not None:
                        old_armor = self.equipped_armor
                        self.defense -= old_armor.effect_value
                        self.inventory.append(old_armor)
                    self.equipped_armor = item
                    self.defense += item.effect_value
                    self.inventory.remove(item)
                    print(f"вы экипировали {item.name}")
            else:
                print(f"предмета {item.name} нет в инвентаре")

        if isinstance(item, Consumable):
            if item in self.inventory:
                print(f"{self.name} использует {item}")
                if item.effect_type == "heal":
                    self.health += item.effect_value
                    print(f"текущее хп {self.name} = {self.health}")
                elif item.effect_type == "buff_defense":
                    self.defense += item.effect_value
                    print(f"текущая защита {self.name} = {self.defense}")
                elif item.effect_type == "buff_attack":
                    self.attack += item.effect_value
                    print(f"текущая атака {self.name} = {self.attack}")
            else:
                print(f"предмета {item.name} нет в инвентаре")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} добавлен в инвентарь {self.name}")

class Mage(Warrior):
    def __init__(self, name, health, attack, defense, equipped_weapon=None, equipped_armor=None):
        super().__init__(name, health, attack, defense)

    def random_get_damage(self, amount):
        actual_damage = random.randint(10, 30), max(amount - self.defense, 0)
        actual_damage += amount
        print(f"урон повысился на: {actual_damage}")
        if self.health <= actual_damage:
            self.health = 0
            print(f"{self.name} повержен!")
        else:
            self.health -= actual_damage
            print(f"{self.name} получает {actual_damage} урона, здоровье: {self.health}")

class Archer(Warrior):
    def __init__(self, name, health, attack, defense, equipped_weapon=None, equipped_armor=None):
        super().__init__(name, health, attack, defense)

    def critical_damage(self, amount):
        actual_damage = random.randint(1, 5)
        if actual_damage == 3:
            amount = self.attack * 1.5
            print("критический урон!")
        else:
            amount = self.attack