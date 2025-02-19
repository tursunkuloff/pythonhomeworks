def second_largest(tpl):
    unique_sorted = sorted(set(tpl), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None


print(second_largest((1, 3, 5, 2, 5)))  
