def get_nested_value(d, outer_key, inner_key):  
    return d.get(outer_key, {}).get(inner_key)  

print(get_nested_value({'a': {'b': 2}}, 'a', 'b'))  
