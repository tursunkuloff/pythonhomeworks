def sum_positive_numbers(lst):
    return sum(num for num in lst if num > 0)


print(sum_positive_numbers([-1, 2, 3, -4, 5]))  
