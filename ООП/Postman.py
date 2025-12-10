from ООП.Person_module import Person  # импортируем класс Person из модуля
from ООП.Post_module import Post  # импортируем класс Post из модуля


class Postman(Person, Post):  # создаём класс Postman (наследуется и от Person, и от Post)
    def __init__(self, name, age, gender, height, weight):  # конструктор принимает данные человека
        Post.__init__(self)  # вызываем конструктор Post для инициализации почтовых атрибутов
        super().__init__(name, age, gender, height, weight)  # вызываем конструктор Person для инициализации данных человека


anna = Postman("Геннадий", 65, "мужской", 210, 100)  # создаём объект Postman

print(anna.name)  # печатаем имя почтового отделения (из Post), а не имя человека
print(anna.send_parcel())  # вызываем метод отправки посылки (вернёт None, потому что внутри только print)
# print(anna.receive_parcel())  # (закомментировано) метод получения посылки
print(anna.parcels)  # выводим словарь посылок почтового отделения