from Items import *
from character import *

class Game:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_running = False
        self.enemies = []
        self.characters_templates = {}
        self.current_player = None

    def start_game(self):
        print("добро пожаловать в игру!")
        self.is_running = True
        self.setup()
        answer = input("выберите персонажа 1-3: воин - 1, маг - 2, лучник - 3")
        if answer == "1":
            print("вы выбрали война!")
        elif answer == "2":
            print("вы выбрали мага!")
        elif answer == "3":
            print("вы выбрали лучника!")
        else:
            print("попробуйте заново")


    def setup(self):
        self.characters_templates = {
            "1": Character("Воин", 100, 20, 15),
            "2": Character("Маг", 70, 35, 5),
            "3": Character("Лучник", 85, 25, 10)}

    def start_battle_loop(self):
        pass

    def stop_game(self):
        answer = input("вы действительно хотите выйти? "
                       "да"
                       "нет")
        if answer == "да":
            self.is_running = False
        else:
            self.is_running = True

class Unit:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.base_defense = defense
        self.base_attack = attack


    def get_damage(self, amount):
        actual_damage = max(amount - self.defense, 0)
        if self.health <= actual_damage:
            print(f"{self.name} повержен!")
        else:
            self.health -= actual_damage
            print(f"{self.name} получает {actual_damage} урона, здоровье: {self.health}")

    def attack_target(self, other_character):
        print(f"{self.name} атакует {other_character.name}!")
        other_character.get_damage(self.attack)

class Character(Unit):
    def __init__(self, name, health, attack, defense,  equipped_weapon = None, equipped_armor = None):
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
                print(f"{self.name} использует {item}")
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

class Enemy(Unit):
    def __init__(self, name, health, defense, attack):
        super().__init__(name, health, attack, defense)