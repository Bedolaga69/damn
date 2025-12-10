# a, b, c = list(map(int, input("введите три числа: ").split()))
# potato = a + b + c - min(a, b, c) - max(a, b, c)
# print("среднее число", potato)
#
#
# a, b, c = map(int, input().split())
# print(min(max(a, min(b, c)), max(b, min(a, c))))


sdf = [12, -2, 65, 154, -78, 76, 90, 657, 823, -10]

m = sdf[0]

for i in sdf:
    if i > m:
        m = i
print(m)