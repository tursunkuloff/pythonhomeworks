text=input("Enter a text:" ).strip()
words=text.split()
if words:
    first_word=words[0]
    last_word=words[-1]
    print("First word:", first_word )
    print("Last word:", last_word )
else:
    print("The input is empty")

