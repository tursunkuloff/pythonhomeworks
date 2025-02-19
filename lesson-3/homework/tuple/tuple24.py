def check_palindrome(tpl):  
    return tpl == tpl[::-1]  


print(check_palindrome((1, 2, 3, 2, 1)))  
print(check_palindrome((1, 2, 3, 4, 5))) 
