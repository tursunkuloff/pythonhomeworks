import os

def create_or_load_file():
    filename = "sample.txt"
    if not os.path.exists(filename):
        print("File 'sample.txt' not found. Please enter a paragraph to create the file:")
        with open(filename, "w") as file:
            text = input("Enter text: ")
            file.write(text)
    with open(filename, "r") as file:
        return file.read()

text = create_or_load_file()
print("File content loaded successfully.")