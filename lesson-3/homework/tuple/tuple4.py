def check_element(tpl, element):
    return element in tpl


print(check_element((1, 2, 3, 4), 3)) 
print(check_element((1, 2, 3, 4), 5))  
