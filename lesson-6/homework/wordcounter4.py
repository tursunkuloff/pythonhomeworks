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

def save_report(word_frequencies, total_words, top_n):
    with open("word_count_report.txt", "w") as file:
        file.write("Word Count Report\n")
        file.write(f"Total Words: {total_words}\n\n")
        file.write("Top Words:\n")
        for word, count in word_frequencies.most_common(top_n):
            file.write(f"{word} - {count}\n")

def main():
    text = create_or_load_file()
    print("File content loaded successfully.")
    
    word_frequencies, total_words = count_word_frequency(text)
    print(f"Total words: {total_words}")
    
    try:
        top_n = int(input("Enter the number of top common words to display: "))
    except ValueError:
        print("Invalid input. Displaying top 5 words by default.")
        top_n = 5
    
    print("Top words:")
    for word, count in word_frequencies.most_common(top_n):
        print(f"{word} - {count} times")
    
    save_report(word_frequencies, total_words, top_n)
    print("Word count report saved to 'word_count_report.txt'.")

if __name__ == "__main__":
    main()