num = int(input("введите число: "))
count = 0
tnuoc = 0
while num > 0:
    d = num % 10
    if d % 2 == 0:
        count += 1
    else:
        tnuoc += 1
    num //= 10
print("кол-во четных цифр: ", count)
print("кол-во нечетных цифр: ", tnuoc)

