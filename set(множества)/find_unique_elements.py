def find_unique_elements(list1, list2):
    l = list1 + list2
    set1 = set(l)
    # print(l)
    return set1

# list4 = list(map(int, input("введите числа 1 списка через пробел: ").split()))
# list5 = list(map(int, input("введите числа 2 списка через пробел: ").split()))

l1 = [5, 6, 87, 2, 45]
l2 = [5, 56, 4, 23, 5]

print(find_unique_elements(l1, l2))


def find_unique_elements2(list1, list2):
    """с методом extend"""
    l = list1.extend(list2)
    set1 = set(l)
    # print(l)
    return set1

# list4 = list(map(int, input("введите числа 1 списка через пробел: ").split()))
# list5 = list(map(int, input("введите числа 2 списка через пробел: ").split()))

l1 = [5, 6, 87, 2, 45]
l2 = [5, 56, 4, 23, 5]

print(find_unique_elements2(l1, l2))
