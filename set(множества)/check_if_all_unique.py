def check_if_all_unique(input_list):
    unique_list = []
    for i in input_list:
        if i in unique_list:
            return False
        unique_list.append(i)#добавление элемента в память что бы помнить что он уже был
    else:#если выхода из цикла не было, то все цифры уникальны
        return True

print(check_if_all_unique([1,2,3,4,5,6,7,8,9,9]))
print(check_if_all_unique([1,2,3,4,5,6,7,8,9]))


def check_if_all_unique2(input_list):
    return len(input_list) == len(set(input_list))