from item_storage import *

class Shop:
    def __init__(self, name: str, assortment: dict):
        self.name = name
        self.assortment = assortment

    def show_items(self):
        print(f'добро пожаловать в магазин {self.name}!')
        print("в продаже:")
        for item_key, item in self.assortment.items():
            print(f"{item_key}, {item.name}: {item.value} монет")

    def buy_item(self, character, item_key):
        if item_key in self.assortment.items():
            buy = self.assortment[item_key]
            if character.gold >= buy.value:
                character.gold -= buy.value
                character.add_item(buy)
                return "покупка состоялась"
            else:
                return "не хватает денег"
        else:
            return "такого товара нет"

    def sell_item(self, character, item_key):
        if item_key in character.inventory:
            print("при продаже предмет теряет 50% от стоимости")
            revenue = item_key.value // 2
            character.gold += revenue
            character.inventory.remove(item_key)
            print(f"персонаж получил: {revenue} золота, баланс: {character.gold}")
        else:
            print("предмета нет в инвентаре")