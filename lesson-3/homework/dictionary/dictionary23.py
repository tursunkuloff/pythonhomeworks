def check_common_keys(d1, d2):  
    return not d1.keys().isdisjoint(d2.keys())  

print(check_common_keys({'a': 1, 'b': 2}, {'b': 3, 'c': 4}))  
