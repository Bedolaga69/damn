from game.game_units import Character
from item_storage import *


class Shop:
    def __init__(self, name: str, assortment: list[Item]):
        self.name = name
        self.assortment = assortment

    def show_items(self):
        print(f'добро пожаловать в магазин {self.name}!')
        print("в продаже:")
        for i in range(len(self.assortment)):
            print(f"{i}, {self.assortment[i].name}: {self.assortment[i].value} монет")

    def buy_item(self, character: Character):
        item_index = int(input("введите номер предмета: "))
        if 0 <= item_index < len(self.assortment):
            item_to_buy = self.assortment[item_index]
            if character.gold >= item_to_buy.value:
                character.gold -= item_to_buy.value
                character.add_item(item_to_buy)
                print("покупка состоялась")
            else:
                print("не хватает денег")
        else:
            print("такого товара нет")

    def sell_item(self, character: Character, item_key: str):
        if item_key in character.inventory:
            print("при продаже предмет теряет 50% от стоимости")
            revenue = item_key.value // 2
            character.gold += revenue
            character.inventory.remove(item_key)
            print(f"персонаж получил: {revenue} золота, баланс: {character.gold}")
        else:
            print("предмета нет в инвентаре")

# shop = Shop("магазинчек", shop_loot.generate_loot())