def first_element(lst):
    if len(lst) == 0: 
        return "List is empty"
    return lst[0] 


my_list = [3, 7, 2, 9, 5]
print(first_element(my_list))  

empty_list = []
print(first_element(empty_list))  