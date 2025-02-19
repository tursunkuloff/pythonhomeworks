def middle_element(lst):
    n = len(lst)
    if n % 2 == 1:
        return lst[n // 2]  
    else:
        return lst[n // 2 - 1:n // 2 + 1]  


print(middle_element([1, 2, 3, 4, 5]))  
print(middle_element([1, 2, 3, 4]))  