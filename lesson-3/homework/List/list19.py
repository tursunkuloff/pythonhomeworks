def replace_element(lst, old, new):
    for i in range(len(lst)):
        if lst[i] == old:
            lst[i] = new
            break
    return lst


my_list = [1, 2, 3, 4, 2]
print(replace_element(my_list, 2, 9)) 
