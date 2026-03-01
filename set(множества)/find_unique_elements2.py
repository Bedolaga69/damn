def find_unique_elements(list1, list2):
    list3 = set(list1).intersection(set(list2))
    return list3


l1 = [1, 2, 4, 5, 1, 2]
l2 = [2, 3, 1, 5, 6, 4]
print(find_unique_elements(l1, l2))