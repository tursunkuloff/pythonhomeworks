def filter_even_numbers(lst):
    return [num for num in lst if num % 2 == 0]


my_list = [1, 2, 3, 4, 5, 6]
print(filter_even_numbers(my_list))