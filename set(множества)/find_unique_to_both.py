def find_unique_to_both(list1, list2):
    list3 = set(list1).symmetric_difference(set(list2))
    return list3

l1 = ['a', 'b', 'c', 'd', 'e', 'f']
l2 = ['a', 'l', 'j', 'q', 'e', 'g']
print(find_unique_to_both(l1, l2))