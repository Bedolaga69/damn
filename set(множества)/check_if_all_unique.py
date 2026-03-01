def check_if_all_unique(input_list):
    unique_list = []
    for i in input_list:
        if i not in unique_list:
            return True
        else:
            return False

print(check_if_all_unique([1,2,3,4,5,6,7,8,9]))