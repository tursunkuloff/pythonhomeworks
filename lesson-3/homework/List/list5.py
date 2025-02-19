def check_element(lst, element):
    for num in lst:  
        if num == element:  
            return True
    return False  

my_list = [3, 7, 2, 9, 5]
print(check_element(my_list, 7))  
print(check_element(my_list, 10)) 
