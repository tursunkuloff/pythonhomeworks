import random  

def generate_random_set(size, start, end):  
    return {random.randint(start, end) for _ in range(size)}  

print(generate_random_set(5, 1, 100)) 
