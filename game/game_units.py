from Items import *

class Unit:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []
        self.max_health = health

    def get_damage(self, amount):
        actual_damage = max(amount - self.defense, 0)
        if self.health <= actual_damage:
            self.health = 0
            print(f"{self.name} повержен!")
        else:
            self.health -= actual_damage
            print(f"{self.name} получает {actual_damage} урона, здоровье: {self.health}")

    def attack_target(self, other_character):
        print(f"{self.name} атакует {other_character.name}!")
        other_character.get_damage(self.attack)

    def is_alive(self):
        return self.health > 0


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




# item_type_list = ["potion", "weapon", "armor", "consumable"]
# effect_type_list = ["heal", "buff_attack", "buff_defense"]
#
#
# potion = Consumable("фласка", "восстанавливает 30 здоровья",95, "heal", 40)
# armor = Equipment("броня", "дает 50 брони", "armor", 50, 250, 25)
# mage_armor = Equipment("мантия", "дает 100 брони", "armor", 125, 150, 50)
# leather_armor = Equipment("кожаные поножи", "дает 25 брони", "armor", 55, 45, 15)
# warrior = Character("воин", 100, 25, 10, None, armor)
# maga = Character("маг", 80, 30, 25, None, mage_armor)
# weapon = Equipment("меч", "дает 33 урона", "weapon", 300, 33, 33)
#
#
# warrior.inventory.append(leather_armor)
# print(warrior.inventory[0])
# warrior.use_item(warrior.inventory[0])
#
# maga.inventory.append(mage_armor)
# maga.inventory.append(potion)
# maga.use_item(mage_armor)
# maga.use_item(potion)
#
# warrior.inventory.append(weapon)
# warrior.use_item(weapon)
#
# warrior.attack_target(maga)
# warrior.inventory.append(potion)
# warrior.use_item(potion)
#
# warrior.use_item(potion)
#
# print(warrior.inventory)