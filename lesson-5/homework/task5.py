def is_prime(n):
    """Returns True if n is a prime number, otherwise False."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  # Check up to √n
        if n % i == 0:
            return False
    return True

# Example usage:
print(is_prime(2))   # True
print(is_prime(10))  # False
print(is_prime(17))  # True
print(is_prime(1))   # False
