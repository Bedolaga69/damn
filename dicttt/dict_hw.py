# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# result = []
#
# for i in a:
#     if i in b and i not in result:
#         result.append(i)
#
# print(result)


# d = {'математика': 3, 'русский': 4, 'обществознание': 5, 'информатика': 8}
#
# for i in d.items():
#     print(f"{i[0]} - {i[1]}")


text = input("введите строку: ")

result = {}

for i in text:
    if i in result:
        result[i] += 1
    else:
        result[i] = 1

print(result)