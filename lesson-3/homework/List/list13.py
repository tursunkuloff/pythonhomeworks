def index_of_element(lst, element):
    for i in range(len(lst)):
        if lst[i] == element:
            return i
    return -1 


my_list = [3, 7, 2, 9, 5]
print(index_of_element(my_list, 2)) 
print(index_of_element(my_list, 10))