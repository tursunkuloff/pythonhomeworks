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
    return word_counts, len(words)

def save_report(word_frequencies, total_words):
    with open("word_count_report.txt", "w") as file:
        file.write(f"Total words: {total_words}\n\n")
        file.write("Top 5 most common words:\n")
        for word, count in word_frequencies.most_common(5):
            file.write(f"{word}: {count}\n")

text = create_or_load_file()
print("File content loaded successfully.")

word_frequencies, total_words = count_word_frequency(text)
print(f"Total words: {total_words}")
print("Top 5 most common words:")
for word, count in word_frequencies.most_common(5):
    print(f"{word}: {count}")

save_report(word_frequencies, total_words)
print("Word count report saved to 'word_count_report.txt'.")