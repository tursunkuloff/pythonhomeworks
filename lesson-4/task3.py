def insert_underscores(txt):
    result = []
    vowels = "aeiouAEIOU"
    i = 0

    while i < len(txt):
        result.append(txt[i])

        
        if (i + 1) % 3 == 0:
            
            if txt[i] in vowels or (i + 1 < len(txt) and txt[i + 1] in vowels):
                if i + 1 < len(txt):
                    result.append(txt[i + 1])
                    i += 1  
            
           
            if i + 1 < len(txt):
                result.append("_")

        i += 1

    return "".join(result)


print(insert_underscores("hello"))       
print(insert_underscores("assalom"))    
print(insert_underscores("abcabcdabcdeabcdefabcdefg"))  

