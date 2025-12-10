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
            if item in self.inventory:
                print(f"{self.name} использует {item}")
                self.inventory.remove(item)
            else:
                print(f"предмет {item} не найден в инвентаре")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{item} добавлен в инвентарь {self.name}")


warrior = Character("воин", 100, 25, 10)
maga = Character("маг", 80, 30, 25)

warrior.add_item("зелье здоровья")
warrior.attack_target(maga)
warrior.use_item("зелье здоровья")