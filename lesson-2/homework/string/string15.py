sentence=input("Enter the sentence:")
acronym="".join(word[0].upper() for word in sentence.split())
print("Acronym:", acronym)