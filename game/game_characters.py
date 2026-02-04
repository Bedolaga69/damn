import random
from game_units import *

class Warrior(Character):
    def __init__(self, name, equipped_weapon=None, equipped_armor=None):
        super().__init__(name, 250, 18, 50, equipped_weapon, equipped_armor)
        # actual_damage = random.randint(1, 5)
        # if actual_damage == 3:
        #     self.attack = self.attack * 1.5
        #     print("критический урон!")
        # else:
        #     self.attack = self.attack
        # print(f"{self.name} атакует {other_character.name}!")
        # other_character.get_damage(self.attack)


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