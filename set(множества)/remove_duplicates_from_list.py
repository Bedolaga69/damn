def remove_duplicates(input_list):
    set1 = set()# помечение чисел которые уже были
    result = []#список для сохранения порядка
    for num in input_list:
        if num not in set1:
            result.append(num)
            set1.add(num)#добавление чтоб не было дубликатов
    return result

print(remove_duplicates([1, 2, 3, 4, 5, 4, 2]))


def filter_unique_guests(guest_list):
    set1 = set()
    g_list = []
    for guest in guest_list:
        if guest not in set1:
            g_list.append(guest)
            set1.add(guest)
    return g_list

print(filter_unique_guests(["андрей", "боря", "кристина", "кристина", "андрей"]))
print(remove_duplicates(["андрей", "боря", "кристина", "кристина", "андрей"]))