from Items import *


class Character:
    def __init__(self, name, health, attack, defense, equipped_weapon=None, equipped_armor=None):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []
        self.equipped_weapon = equipped_weapon
        self.equipped_armor = equipped_armor

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

    def use_item(self, item):
        if item in self.inventory:
            print(f"{self.name} использует {item.name if hasattr(item, 'name') else item}")

            if isinstance(item, Equipment):
                if item.equipment_type == "weapon":
                    if self.equipped_weapon is not None:
                        old_weapon = self.equipped_weapon
                        self.attack -= old_weapon.effect_value
                        self.inventory.append(old_weapon)
                    self.equipped_weapon = item
                    self.attack += item.effect_value
                    self.inventory.remove(item)  # Удаляем после экипировки
                    print(f"вы экипировали {item.name}")
                elif item.equipment_type == "armor":
                    if self.equipped_armor is not None:
                        old_armor = self.equipped_armor
                        self.defense -= old_armor.effect_value
                        self.inventory.append(old_armor)
                    self.equipped_armor = item
                    self.defense += item.effect_value
                    self.inventory.remove(item)  # Удаляем после экипировки
                    print(f"вы экипировали {item.name}")

            elif isinstance(item, Consumable):
                if item.effect_type == "heal":
                    self.health += item.effect_value
                    print(f"текущее хп {self.name} = {self.health}")
                elif item.effect_type == "buff_defense":
                    self.defense += item.effect_value
                    print(f"текущая защита {self.name} = {self.defense}")
                elif item.effect_type == "buff_attack":
                    self.attack += item.effect_value
                    print(f"текущая атака {self.name} = {self.attack}")
                self.inventory.remove(item)  # Удаляем после использования
        else:
            print(f"предмет {item.name if hasattr(item, 'name') else item} не найден в инвентаре")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item.name if hasattr(item, 'name') else item} добавлен в инвентарь {self.name}")


# Создание объектов
potion = Consumable("фласка", "восстанавливает 30 здоровья", 95, "heal", 40)
armor = Equipment("броня", "дает 50 брони", "armor", 50, 250, 25)
mage_armor = Equipment("мантия", "дает 100 брони", "armor", 125, 150, 50)
leather_armor = Equipment("кожанные поножи", "дает 25 брони", "armor", 55, 45, 15)

# Создание персонажей
warrior = Character("воин", 100, 25, 10, None, armor)
maga = Character("маг", 80, 30, 25, None, mage_armor)

# Тестирование
warrior.inventory.append(leather_armor)
print(warrior.inventory[0].name)  # Изменено: выводим имя

# Используем предмет из инвентаря
if leather_armor in warrior.inventory:
    warrior.use_item(leather_armor)

warrior.add_item(potion)  # Добавляем зелье в инвентарь
warrior.attack_target(maga)

# Используем зелье (теперь оно в инвентаре)
if potion in warrior.inventory:
    warrior.use_item(potion)