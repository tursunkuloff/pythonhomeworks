def check(func):
    def wrapper():
        a = float(input("Enter numerator: "))
        b = float(input("Enter denominator: "))
        if b == 0:
            return "Denominator can't be zero"
        return func(a, b)
    return wrapper

@check
def div(a, b):
    return a / b

# Test case
print(div())