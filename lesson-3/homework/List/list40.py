def get_unique_elements(lst):
    seen = set()
    unique_list = []
    for item in lst:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list


print(get_unique_elements([1, 2, 2, 3, 4, 3, 5]))  

