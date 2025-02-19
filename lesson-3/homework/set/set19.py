def merge_and_deduplicate(lst1, lst2):  
    return set(lst1) | set(lst2)  

print(merge_and_deduplicate([1, 2, 2, 3], [3, 4, 4, 5]))  
