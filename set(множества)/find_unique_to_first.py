def find_unique_elements(list1, list2):
    list3 = set(list1).difference(set(list2))
    return list3

l1 = ['a', 'b', 'c', 'd', 'e', 'f']
l2 = ['a', 'l', 'j', 'q', 'e', 'g']
print(find_unique_elements(l1, l2))