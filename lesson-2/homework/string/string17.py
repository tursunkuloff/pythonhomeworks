text=input("Enter a string: ")
symbol=input("Enter the symbol to replace vowel: ")
vowels="AEIOUaeiou"
for vowel in vowels:
    text = text.replace(vowel, symbol)
    
print("Modified string:", text)
