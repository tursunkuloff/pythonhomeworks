def last_element(lst):
    if len(lst) == 0:  
        return "List is empty"
    return lst[-1] 


my_list = [3, 7, 2, 9, 5]
print(last_element(my_list)) 

empty_list = []
print(last_element(empty_list)) 