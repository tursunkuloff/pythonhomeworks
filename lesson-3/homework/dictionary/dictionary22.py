def filter_by_value(d, condition):  
    return {k: v for k, v in d.items() if condition(v)}  

print(filter_by_value({'a': 3, 'b': 1, 'c': 2}, lambda x: x > 1))  
