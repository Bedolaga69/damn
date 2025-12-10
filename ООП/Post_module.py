import random  # импортируем модуль random для генерации случайных чисел


class Post:  # создаём класс Post (почтовое отделение)

    def __init__(self, name, post_id):  # конструктор вызывается при создании объекта Post
        self._parcels = {}  # словарь посылок, хранит {id: название}
        self._name = name # имя почтового отделения
        self._post_id = post_id # уникальный id почтового отделения
        self._id_password = {}  # словарь паролей {id: пароль}
        print("Объект создан")  # сообщение в консоль при создании объекта

    @property  # превращает метод в геттер
    def name(self):  # метод-геттер для имени почтового отделения
        return self._name  # возвращаем значение _name

    @property  # превращает метод в геттер
    def id(self):  # метод-геттер для id почтового отделения
        return self._post_id  # возвращаем значение _post_id

    @name.setter  # превращает метод в сеттер
    def name(self, new_name):  # метод-сеттер для изменения имени почтового отделения
        self._name = new_name  # записываем новое имя в _name

    @property  # превращает метод в геттер
    def parcels(self):  # метод-геттер для получения всех посылок
        return self._parcels  # возвращаем словарь посылок

    def __str__(self):
        return f"{self._name}, {self._post_id}"

    def __generate_id(self):  # приватный метод для генерации уникального id посылки
        while True:  # бесконечный цикл до тех пор, пока не найдём уникальный id
            parcel_id = str(random.randint(100, 999))  # генерируем случайное число от 100 до 999 и делаем строкой
            if parcel_id not in self._parcels:  # проверяем, что id ещё не занят
                return parcel_id  # возвращаем уникальный id

    def send_parcel(self):  # метод для отправки посылки
        parcel_name = input("введите название посылки: ")  # просим ввести название посылки
        parcel_id = self.__generate_id()  # генерируем уникальный id для посылки
        self._parcels[parcel_id] = parcel_name  # сохраняем посылку в словаре
        password = input(f"введите пароль для посылки {parcel_id}: ")  # просим ввести пароль для этой посылки
        self._id_password[parcel_id] = password  # сохраняем пароль в словарь паролей
        print(f"посылка {parcel_name} успешно отправлена, id {parcel_id}")  # выводим подтверждение отправки

    def receive_parcel(self):  # метод для получения посылки
        parcel_id = input("введите id посылки: ")  # запрашиваем id посылки
        if parcel_id in self._parcels:  # проверяем, есть ли посылка с таким id
            password = input("введите пароль: ")  # запрашиваем пароль
            if password == self._id_password[parcel_id]:  # проверяем правильность пароля
                del self._parcels[parcel_id]  # удаляем посылку (считаем, что получена)
                print(f"посылка {parcel_id} получена")  # сообщение об успешном получении
            else:
                print("неверный пароль")  # сообщение при неправильном пароле
        else:
            print(f"посылка с id {parcel_id} не найдена")  # сообщение, если id нет в словаре


# post = Post()  # создаём объект Post, сразу печатается «Объект создан»
#
# post.send_parcel()  # отправляем первую посылку (будет ввод названия и пароля)
#
# post.send_parcel()  # отправляем вторую посылку (будет ввод)
#
# # print(post.Post_parcels)  #  попытка вывести приватный атрибут, не рекомендуется
# print(post.parcels)  # выводим словарь посылок через геттер
#
# # print(post.name)  #  печать имени почтового отделения
# # print(post.id)  #  печать id почтового отделения
#
# post.receive_parcel()  # пытаемся получить посылку (будет ввод id и пароля)
#
# # print(post.parcels)  #  вывод словаря посылок после получения
# # print(post.Post_id_password)  #  печать словаря паролей (не рекомендуется)