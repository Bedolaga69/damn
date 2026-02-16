from game_characters import *
from game_units import *
from item_storage import *
import random

class Game:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.is_running = False
        self.enemies = []
        self.characters_templates = {}
        self.current_player = None
        self.current_enemy = None


    def start_game(self):
        print("добро пожаловать в игру!")
        self.is_running = True
        self.characters_templates = {
            "1": Warrior,
            "2": Mage,
            "3": Archer
        }
        answer = input("выберите персонажа 1-3: воин - 1, маг - 2, лучник - 3 :")
        if answer in self.characters_templates:
            char_name = input("введите имя героя: ")
            ClassType = self.characters_templates[answer]
            self.current_player = ClassType(name=char_name)
            print(f"\nвы выбрали {self.current_player.name}")
            print(f"по умолчанию у вас: {self.current_player.add_item(Consumable("зелье здоровья", "восстанавливает 30 здоровья",95, "heal", 30))}")
        else:
            self.current_player = self.characters_templates["1"]("воин")
            print("некорректный выбор, по умолчанию выбран воин")
            print(f"по умолчанию у вас: {self.current_player.add_item(Consumable("зелье здоровья", "восстанавливает 30 здоровья", 95, "heal", 30))}")
        self._create_default_enemies(4)
        self._start_battle_loop()


    def _create_default_enemies(self, count):
            """Приватный метод для создания набора врагов."""
            enemy_templates = [
                ("Гоблин", 28, 8, 7),
                ("Орк", 100, 12, 13),
                ("Скелет", 50, 10, 5)
            ]

            for i in range(count):
                # Выбираем шаблон врага циклически
                template = enemy_templates[i % len(enemy_templates)]
                name, hp, atk, dfns = template
                self.enemies.append(Enemy(f"{name} {i+1}", hp, atk, dfns))

            print(f"вы оглянулись и увидели {len(self.enemies)} врагов")

    def _start_battle_loop(self):
        while self.current_player.is_alive() and len(self.enemies) > 0: #проверка на хп игрока и на то есть ли враги
            self._process_player_action()# Вызываем ход игрока
            if not self.is_running:
                break
            if len(self.enemies) > 0:# проверка есть ли враги
                self._process_enemy_turn()# если есть, то атакуют

        if self.current_player.is_alive():# проверка на хп игрока
            if len(self.enemies) > 0:
                rndm = random.randint(0, 3)
                if rndm == 2:
                    print("вам повезло! вы убежали от врагов")
                else:
                    print("вы проиграли, у вас не получилось убежать...")
                    self.is_running = False
            else:
                print("победа!!!!!!!!!!!")
        else:
            print("вы проиграли, игра окончена...")
            self.is_running = False

    def _process_player_action(self):
        """метод для обработки выбора игрока"""
        # if self.is_running:
        print(f"моя защита: {self.current_player.defense}, мое HP: {self.current_player.health}/{self.current_player.max_health}")
        current_target = self.enemies[0]
        print(f"Противник: {current_target.name} (HP: {current_target.health})")
        while True:
            answer = input("что вы хотите сделать?"
                               "\n1 - атаковать"
                               "\n2 - использовать предмет"
                               "\n3 - убежать: ")

            if answer == "1":
                self.current_player.attack_target(current_target)


                if not current_target.is_alive(): # проверка на живучесть цели после удара
                    print(f"враг {current_target.name} мертв")
                    self.enemies.pop(0)
                    self.current_player.reset_damage()
                else:
                    self.current_player.buff_damage()
                break


            elif answer == "2":
                print(f"ваш инвентарь: {self.current_player.inventory}")
                item_answer = input("введите порядковый номер предмета: ")#поменять инт и сделать его как отдельную проверку от инпута т.е сначала инпут потом уже проверка на число ли это
                if item_answer.isdigit():
                    item_answer = int(item_answer)
                    if len(self.current_player.inventory) >= item_answer:
                        self.current_player.use_item(self.current_player.inventory[item_answer - 1])
                        break
                    else:
                        print("такого предмета в инвентаре нет")
                else:
                    print("вы ввели не число, повторите ввод")

            elif answer == "3":
                self.is_running = False
                break

            else:
                print("введено не правильное число")


    def _process_enemy_turn(self):
        """Метод для автоматического хода противника"""
        # if self.is_running:
        attaker = self.enemies[0]
        print(f"ход врага {attaker.name}")
        attaker.attack_target(self.current_player)
        # self.enemies.pop(0)

    def stop_game(self):
        answer = input("вы действительно хотите выйти? "
                       "\nда"
                       "\nнет: ")
        if answer == "да":
            self.is_running = False
        else:
            self.is_running = True


game = Game("подземелье колодца", "приключение в подземелье")
game.start_game()