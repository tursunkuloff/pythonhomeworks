def uncommon_elements(list1, list2):
    
    freq1 = {}
    freq2 = {}

   
    for num in list1:
        freq1[num] = freq1.get(num, 0) + 1

 
    for num in list2:
        freq2[num] = freq2.get(num, 0) + 1

    result = []

    
    for num in list1:
        if num not in freq2:
            result.append(num)

 
    for num in list2:
        if num not in freq1:
            result.append(num)

    return result


print(uncommon_elements([1, 1, 2], [2, 3, 4]))      
print(uncommon_elements([1, 2, 3], [4, 5, 6]))      
print(uncommon_elements([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))  
