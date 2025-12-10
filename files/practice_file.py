# with open('newfile.txt', 'w', encoding='utf-8') as g:
#     d = int(input("введите число: "))
#     print(f'1 / {d} = {1 / d}', file=g)
#
#
# a = [34, 45]
# b = a
# print([1, 2, 3] is [1, 2, 3])
# print([1, 2, 3] == [1, 2, 3])
# print(a is b)
# print()
# print(type(a) is type(b))

with open("gyat.txt", "w") as b:
    while True:
        user_input = input("Введите команду (stop чтобы остановить): ")
        if user_input == "stop":
            break
        else:
            b.write("N\n")