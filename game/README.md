

## Shop

 - [class Shop]("C:\Users\MSI\PycharmProjects\damn\game\Shop.py"), принимает атрибуты имя и список ассортимента предметов
 - [def show_items]("C:\Users\MSI\PycharmProjects\damn\game\Shop.py"), показывает все предметы в магазине
 - [def buy_item]("C:\Users\MSI\PycharmProjects\damn\game\Shop.py"), покупка предмета по его номеру 
 - [def sell_item]("C:\Users\MSI\PycharmProjects\damn\game\Shop.py"), продажа предмета с комиссией магазина
 
## Game 
 - [class Game]("C:\Users\MSI\PycharmProjects\damn\game\game.py"), принимает атрибуты имя и описание
 - [def start_game]("C:\Users\MSI\PycharmProjects\damn\game\game.py"), начало игры с выбором персонажа из возможных и базовым инвентарем для каждого из них
 - [def _create_default_enemies]("C:\Users\MSI\PycharmProjects\damn\game\game.py"), приватный метод для создания набора врагов
 - [def _start_battle_loop]("C:\Users\MSI\PycharmProjects\damn\game\game.py"), начало игрового лупа с ходом игрока и врага, и возможность убежать от врагов
 - [def start_shop_event]("C:\Users\MSI\PycharmProjects\damn\game\game.py"), открытие магазина как "временный ивент"
 - [def _process_player_action]("C:\Users\MSI\PycharmProjects\damn\game\game.py"), метод для обработки выбора игрока
 - [def _process_enemy_turn]("C:\Users\MSI\PycharmProjects\damn\game\game.py"), метод для автоматического хода врага
 - [def stop_game]("C:\Users\MSI\PycharmProjects\damn\game\game.py"), метод для завершения игры