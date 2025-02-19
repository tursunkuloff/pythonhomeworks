def second_largest(lst):
    unique_lst = list(set(lst))  
    unique_lst.sort(reverse=True)  
    return unique_lst[1] if len(unique_lst) > 1 else None


my_list = [1, 2, 3, 4, 4, 5]
print(second_largest(my_list))  