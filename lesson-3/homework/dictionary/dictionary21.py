def sort_dict_by_value(d):  
    return dict(sorted(d.items(), key=lambda item: item[1]))  

print(sort_dict_by_value({'a': 3, 'b': 1, 'c': 2}))  
