from game_units import *


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
            "1": Character("Воин", 100, 20, 15),
            "2": Character("Маг", 70, 35, 5),
            "3": Character("Лучник", 85, 25, 10)}
        answer = input("выберите персонажа 1-3: воин - 1, маг - 2, лучник - 3 :")
        if answer == "1":
            self.current_player = self.characters_templates["1"]
            print("вы выбрали война!")
        elif answer == "2":
            self.current_player = self.characters_templates["2"]
            print("вы выбрали мага!")
        elif answer == "3":
            self.current_player = self.characters_templates["3"]
            print("вы выбрали лучника!")
        else:
            self.current_player = self.characters_templates["1"]
            print("некорректный выбор, по умолчанию выбран воин")
        self._create_default_enemies(4)
        self._start_battle_loop()


    def _create_default_enemies(self, count):
            """Приватный метод для создания набора врагов."""
            enemy_templates = [
                ("Гоблин", 28, 8, 15),
                ("Орк", 100, 12, 30),
                ("Скелет", 50, 10, 15)
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

            if len(self.enemies) > 0:# проверка есть ли враги
                self._process_enemy_turn()# если есть, то атакуют

        if self.current_player.is_alive() <= 0:# проверка на хп игрока
            print("вы проиграли... игра окончена!")
            self.is_running = False
        else:
            print("победа! все враги повержены!")

    def _process_player_action(self):
        """метод для обработки выбора игрока"""
        print(f"моя защита: {self.current_player.defense}, мое HP: {self.current_player.health}/{self.current_player.max_health}")
        current_target = self.enemies[0]
        print(f"Противник: {current_target.name} (HP: {current_target.health})")

        answer = input("что вы хотите сделать?"
                           "\n1 - атаковать"
                           "\n2 - использовать предмет: ")

        if answer == "1":
            target = self.enemies[0]
            self.current_player.attack_target(target)

            if not target.is_alive(): # проверка на живучесть цели после удара
                print(f"враг {target.name} мертв")
                self.enemies.pop(0)
        # elif answer == "2":
        #     target = self.enemies[0]
    def _process_enemy_turn(self):
        """Метод для автоматического хода противника"""
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