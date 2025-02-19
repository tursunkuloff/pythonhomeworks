def max_element(lst):
    max_num = lst[0]  
    for num in lst:  
        if num > max_num:  
            max_num = num
    return max_num  
my_list = [3, 7, 2, 9, 5]
print(max_element(my_list))