text=input("Enter a string:").lower()
vowels="aeiou"
vowel_count=sum(1 for char in text if char in vowels)
consonant_count=sum(1 for char in text if char.isalpha()and char not in vowels)
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)
