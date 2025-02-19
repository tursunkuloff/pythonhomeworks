def get_unique_elements(tpl):  
    seen = set()  
    return tuple(x for x in tpl if not (x in seen or seen.add(x)))  

  
print(get_unique_elements((1, 2, 2, 3, 4, 4, 5)))   
print(get_unique_elements((5, 5, 5, 5, 5))) 
