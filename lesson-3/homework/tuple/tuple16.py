def is_tuple_sorted(tpl):
    return tpl == tuple(sorted(tpl))


print(is_tuple_sorted((1, 2, 3)))  
print(is_tuple_sorted((3, 1, 2)))  
