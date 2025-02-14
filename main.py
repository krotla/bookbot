
def main():
    file_path = "books/frankenstein.txt"
    text = load_text(file_path)
    words_number = count_words(text)
    char_counts = count_chars(text)
    char_counts_sorted = dict_to_sorted_list(char_counts)
    print_report(file_path, words_number, char_counts_sorted)
    
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

def dict_to_sorted_list(dictionary):
    new_list = []
    for key in dictionary:
        new_list.append({"char": key, "count": dictionary[key]})
    new_list.sort(key=sort_on, reverse=True)
    return new_list

def sort_on(dictionary):
    return dictionary["count"]

def print_report(file_path, words_number, char_counts):
    print(f"--- Begin report of {file_path} ---")
    print(f"{words_number} words found in the document\n")
    for char_info in char_counts:
        if char_info["char"].isalpha():
            print(f"The '{char_info["char"]}' character was found {char_info["count"]} times")
    print("--- End report ---")


main()