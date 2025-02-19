def count_even_numbers(lst):
    count = 0
    for num in lst:
        if num % 2 == 0:
            count += 1
    return count


my_list = [3, 7, 2, 9, 4, 6]
print(count_even_numbers(my_list)) 