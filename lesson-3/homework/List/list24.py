def list_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


my_list = [1, 2, 3, 4, 5]
print(list_length(my_list)) 
