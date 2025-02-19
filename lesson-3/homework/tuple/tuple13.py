def second_smallest(tpl):
    unique_sorted = sorted(set(tpl))
    return unique_sorted[1] if len(unique_sorted) > 1 else None


print(second_smallest((1, 3, 5, 2, 5)))  
