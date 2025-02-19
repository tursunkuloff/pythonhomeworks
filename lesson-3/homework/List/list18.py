def find_sublist(lst, sublst):
    for i in range(len(lst) - len(sublst) + 1):
        if lst[i:i + len(sublst)] == sublst:
            return True
    return False


main_list = [1, 2, 3, 4, 5]
sub_list = [2, 3]
print(find_sublist(main_list, sub_list))  

not_in_list = [3, 5]
print(find_sublist(main_list, not_in_list)) 
