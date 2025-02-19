def find_all_indices(lst, element):
    return [i for i, x in enumerate(lst) if x == element]


print(find_all_indices([1, 2, 3, 2, 4, 2], 2)) 
