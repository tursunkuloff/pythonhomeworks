def check_for_nested_dicts(d):  
    return any(isinstance(v, dict) for v in d.values())  

print(check_for_nested_dicts({'a': 1, 'b': {'c': 2}})) 
