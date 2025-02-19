def remove_by_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    return lst


my_list = [1, 2, 3, 4, 5]
print(remove_by_index(my_list, 2)) 
