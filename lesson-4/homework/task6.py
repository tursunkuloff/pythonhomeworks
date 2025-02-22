print("Prime numbers between 1 and 100:")

for num in range(2, 101):  
    is_prime = True  
    for divisor in range(2, num):  
        if num % divisor == 0:
            is_prime = False  
            break  
    if is_prime:
        print(num, end=" ")
