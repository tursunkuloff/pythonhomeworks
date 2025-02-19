from collections import defaultdict  

def create_default_dict(default_value):  
    return defaultdict(lambda: default_value)  

d = create_default_dict(0)  
print(d['unknown'])  
