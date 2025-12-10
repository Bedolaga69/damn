# l = []
# t = ()
# d = {}

# print(type(l), type(t), type(d), sep="\n")

# d={"dict": 1, "dictionary": 2}
# print(d["dict"])
#
# d = dict(short='dict', long='dictionary', kek='lol')
# print(d)

# d = dict([(1, 1), (2, 4), ('kek', 'lol')])
# print(d)
#
# d = dict.fromkeys(['a', 'b', 'd'], 12)
# print(d)
#
# d["a"]+=1
# print(d)
# d["b"]="aboba"
# print(d)
#
# print([1, 'a', [1, 3]])
#
# c = [j*3 for j in range(1, 100)]
# print(c)
#
# d = {a: a ** 2 for a in range(7)}
# print(d)

#dict методы


# dict.clear()
# очищает словарь, удаляя все элементы.

# d = {'a': 1, 'b': 2}
# d.clear()
# print(d) # Вывод: {}

# dict.copy()
# Возвращает поверхностную копию словаря.
#
# d = {'a': 1, 'b': 2}
# d_copy = d.copy()
# print(d_copy)  # Вывод: {'a': 1, 'b': 2}
#
# dict.fromkeys(seq[, value])
# Создает новый словарь с ключами из последовательности seq и значениями value (по умолчанию None).
# Пример:
#
# keys = ['a', 'b', 'c']
# d = dict.fromkeys(keys, 0)
# print(d)  # Вывод: {'a': 0, 'b': 0, 'c': 0}
#
# dict.get(key[, default])
# Возвращает значение для ключа key, если ключ существует. Если ключ отсутствует, возвращает default (по умолчанию None).
# Пример:
#
# d = {'a': 1, 'b': 2}
# print(d.get('a'))  # Вывод: 1
# print(d.get('c', 'Ключ не найден'))  # Вывод: 'Ключ не найден'
#
# dict.items()
# Возвращает представление пар (ключ, значение) словаря.
# Пример:
#
# d = {'a': 1, 'b': 2}
# print(d.items())  # Вывод: dict_items([('a', 1), ('b', 2)])
#
# dict.keys()
# Возвращает представление ключей словаря.
# Пример:
#
# d = {'a': 1, 'b': 2}
# print(d.keys())  # Вывод: dict_keys(['a', 'b'])
#
# dict.pop(key[, default])
# Удаляет ключ key и возвращает его значение. Если ключ отсутствует и указан default, возвращает его.
# В противном случае вызывает исключение.
# Пример:
#
# d = {'a': 1, 'b': 2}
# value = d.pop('a')
# print(value)  # Вывод: 1
# print(d)      # Вывод: {'b': 2}
#
# dict.popitem()
# Удаляет и возвращает последнюю добавленную пару (ключ, значение). Если словарь пуст, вызывает исключение KeyError.
# Пример:
#
# d = {'a': 1, 'b': 2}
# item = d.popitem()
# print(item)  # Вывод: ('b', 2)
# print(d)     # Вывод: {'a': 1}
#
# dict.setdefault(key[, default])
# Возвращает значение ключа key, если он существует. Если ключ отсутствует,
# вставляет его со значением default (по умолчанию None) и возвращает это значение.
# Пример:
#
# d = {'a': 1}
# value = d.setdefault('b', 2)
# print(value)  # Вывод: 2
# print(d)      # Вывод: {'a': 1, 'b': 2}
#
# dict.update([other])
# Обновляет словарь, добавляя пары (ключ, значение) из другого словаря other. Существующие ключи перезаписываются.
# Пример:
#
# d = {'a': 1}
# d.update({'b': 2, 'a': 3})
# print(d)  # Вывод: {'a': 3, 'b': 2}
#
# dict.values()
# Возвращает представление значений словаря.
# Пример:
#
# d = {'a': 1, 'b': 2}
# print(d.values())  # Вывод: dict_values([1, 2])