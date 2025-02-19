def insert_element(lst, element, index):
    lst.insert(index, element)
    return lst

my_list = [3, 7, 2, 9, 5]
print(insert_element(my_list, 10, 2))