def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = word_count(text)
    chars_dict = get_char_count(text)
    chars_sorted_list = split_and_label_dict(chars_dict)

    print(f"--- Begin report of {book_path}")
    print(f"{num_words} words found in the document")
    print()

    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

    

def get_book_text(path):
    with open(path) as f:
        return f.read()

def word_count(book_text):
    words = book_text.split()
    return len(words)

def get_char_count(chars):
    char_count = {}
    lowered_chars = chars.lower()
    for i in lowered_chars:
        if i in char_count:
            char_count[i] += 1
        else:
            char_count[i] = 1
    return char_count

def split_and_label_dict(input_dict):
    split_list = []
    for i in input_dict:
        split_list.append({"char": i, "num": input_dict[i]})
    split_list.sort(reverse=True, key=sort_on)
    return split_list

def sort_on(d):
    return d["num"]



main()