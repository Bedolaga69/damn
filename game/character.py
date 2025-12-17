class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense
        self.inventory = []

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
        if isinstance(item, Consumable):
            if item in self.inventory:
                print(f"{self.name} использует {item}")
                self.inventory.remove(item)
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
                print(f"предмет {item} не найден в инвентаре")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} добавлен в инвентарь {self.name}")


item_type_list = ["potion", "weapon", "armor", "consumable"]
effect_type_list = ["heal", "buff_attack", "buff_defense"]


potion = Consumable("фласка", "восстанавливает 30 здоровья",95, "лечение", 40)
armor = Equipment("броня", "дает 50 брони", "нагрудник", 50, 250)
warrior = Character("воин", 100, 25, 10)
maga = Character("маг", 80, 30, 25)

warrior.add_item("зелье здоровья")
warrior.attack_target(maga)
warrior.use_item("зелье здоровья")