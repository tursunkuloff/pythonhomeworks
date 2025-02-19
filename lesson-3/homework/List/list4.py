def min_element(lst):
    min_num = lst[0]  
    for num in lst:  
        if num < min_num:  
            min_num = num
    return min_num 


my_list = [3, 7, 2, 9, 5]
print(min_element(my_list))  
