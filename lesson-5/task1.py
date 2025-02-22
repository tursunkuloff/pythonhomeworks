def convert_cel_to_far(celsius):
    """Convert Celsius to Fahrenheit"""
    return round(celsius * 9 / 5 + 32, 2)

def convert_far_to_cel(fahrenheit):
    """Convert Fahrenheit to Celsius"""
    return round((fahrenheit - 32) * 5 / 9, 2)


fahrenheit = float(input("Enter a temperature in degrees F: "))
celsius_result = convert_far_to_cel(fahrenheit)
print(f"{fahrenheit} degrees F = {celsius_result} degrees C\n")


celsius = float(input("Enter a temperature in degrees C: "))
fahrenheit_result = convert_cel_to_far(celsius)
print(f"{celsius} degrees C = {fahrenheit_result} degrees F")
