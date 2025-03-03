import os
import string
from collections import Counter

def create_or_load_file():
    filename = "sample.txt"
    if not os.path.exists(filename):
        print("File 'sample.txt' not found. Please enter a paragraph to create the file:")
        with open(filename, "w") as file:
            text = input("Enter text: ")
            file.write(text)
    with open(filename, "r") as file:
        return file.read()

def count_word_frequency(text):
    text = text.lower().translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    word_counts = Counter(words)
    return word_counts

text = create_or_load_file()
print("File content loaded successfully.")

word_frequencies = count_word_frequency(text)
print("Word Frequencies:")
for word, count in word_frequencies.items():
    print(f"{word}: {count}")
