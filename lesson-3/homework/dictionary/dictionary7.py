def remove_key(d, key):  
    d.pop(key, None)  
    return d  

print(remove_key({'a': 1, 'b': 2, 'c': 3}, 'b'))  
