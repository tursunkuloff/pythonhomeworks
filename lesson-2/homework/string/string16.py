string=input("Enter a string:")
character=input("Enter a character you want to remove from string")
if character in string:
    new_word=string.replace(character, "")
    print("Mentioned character is removed:", new_word)
else:
    print("The string does not have this character")