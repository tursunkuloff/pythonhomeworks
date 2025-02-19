def get_all_indices(tpl, element):
    return [i for i, x in enumerate(tpl) if x == element]


print(get_all_indices((1, 2, 3, 2, 4, 2), 2)) 
