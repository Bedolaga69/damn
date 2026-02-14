from decimal import Decimal
import random

from game_units import *

class Warrior(Character):
    def __init__(self, name, equipped_weapon=None, equipped_armor=None):
        super().__init__(name, 250, 18, 50, equipped_weapon, equipped_armor)
        self.multiplier_damage = 1.0

    def attack_target(self, other_character):
        actual_damage = self.attack * self.multiplier_damage#round - округление до 2 знаков после запятой
        print(f"урон повысился до {actual_damage}")
        print(f"{self.name} атакует {other_character.name}!")
        other_character.get_damage(actual_damage)

    def buff_damage(self):
        self.multiplier_damage += 0.1

    def reset_damage(self):
        self.multiplier_damage = 1.0
        print(f"урон у {self.name} сбросился до {self.attack}")

class Mage(Character):
    def __init__(self, name, equipped_weapon=None, equipped_armor=None):
        super().__init__(name, 150, 21, 20, equipped_weapon, equipped_armor)

    def attack_target(self,other_character):
        actual_damage = random.randint(self.attack + 5, self.attack + 15)
        print(f"урон повысился до: {actual_damage}")
        print(f"{self.name} атакует {other_character.name}!")
        other_character.get_damage(actual_damage)

class Archer(Character):
    def __init__(self, name, equipped_weapon=None, equipped_armor=None):
        super().__init__(name, 200, 20, 10, equipped_weapon, equipped_armor)

    def attack_target(self,other_character):
        actual_damage = self.attack
        if random.randint(1, 5) == 3:
            actual_damage = self.attack * 1.5
            print("критический урон!")
        print(f"{self.name} атакует {other_character.name}!")
        other_character.get_damage(actual_damage)