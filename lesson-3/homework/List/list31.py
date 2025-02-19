def repeat_elements(lst, n):
    return [elem for elem in lst for _ in range(n)]


print(repeat_elements([1, 2, 3], 2))  
