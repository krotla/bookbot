
def main():
    file_path = "books/frankenstein.txt"
    text = load_text(file_path)
    words_number = count_words(text)
    char_counts = count_chars(text)
    print_report(file_path, words_number, char_counts)
    
def load_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_chars(text):
    char_counts = {}
    text = text.lower()
    for i in range(0, len(text)):
        character = text[i]
        if character in char_counts:
            char_counts[character] += 1
        else:
            char_counts[character] = 1
    return char_counts

def print_report(file_path, words_number, char_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{words_number} words found in the document\n")
    for c in char_counts:
        if c.isalpha():
            print(f"The '{c}' character was found {char_counts[c]} times")
    print("--- End report ---")


main()