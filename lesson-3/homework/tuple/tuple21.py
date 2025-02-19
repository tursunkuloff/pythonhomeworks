def repeat_elements(tpl, n):
    return tuple(x for x in tpl for _ in range(n))


print(repeat_elements((1, 2, 3), 2))  
