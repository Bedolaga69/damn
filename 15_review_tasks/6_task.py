"""Словарь из строк: Дан список слов. Создай словарь, где ключом будет само слово, а значением — количество букв в нем."""

words = ["apple", "pie", "juice"]
result = {}
for word in words:
    result[word] = len(word)
print(result)

names = ["alise", "bob", "charlie", "david"]
result = {}
for name in names:
    result[name] = name[0]
print(result)

numbers = [1, 2, 3, 4, 5]
parity_dict = {}
for number in numbers:
    if number % 2 == 0:
        parity_dict[number] = "even"
    else:
        parity_dict[number] = "odd"

print(parity_dict)

fruits = ["apple", "banana", "cherry", "aboba"]
result = {}
for fruit in fruits:
    if fruit[0] == "a":
        result[fruit] = "starts with a"
    else:
        result[fruit] = "other"
print(result)