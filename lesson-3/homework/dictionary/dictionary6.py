def merge_dictionaries(d1, d2):  
    return {**d1, **d2}  

print(merge_dictionaries({'a': 1, 'b': 2}, {'b': 3, 'c': 4})) 
