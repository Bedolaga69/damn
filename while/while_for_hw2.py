# n = int(input("введите число: "))
#
# factorial = 1
# for i in range(1, n + 1):
#     factorial *= i
#
# print(f"{n}! = {factorial}")

# n = int(input("Введите число: "))
#
# fact = 1
# i = 1
# while i <= n:
#     fact *= i
#     i += 1
# print(f"{n}! = {fact}")


x1, y1, x2, y2 = map(int, input().split())
if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
    print(x1, y1, x2, y2)
    #король
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1 and not (x1 - x2 == 0 and y1 - y2 == 0): #abs() модуль
        print("король может сделать ход")
    else:
        print("король не может сделать ход")
    #ладья
    if x1 == x2 or y1 == y2:
        print("ладья может сделать ход")
    else:
        print("ладья не может сделать ход")
else:
    print("ошибка")
