text=str(input("Enter the word:"))
text=text.lower()
if text==text[::-1]: print("The word is palindrome")
else: print("The word is not palindrome")