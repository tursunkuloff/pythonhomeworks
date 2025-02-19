def get_first_key_value_pair(d):  
    return next(iter(d.items()), None)  

print(get_first_key_value_pair({'a': 1, 'b': 2}))  
