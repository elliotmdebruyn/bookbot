import sys
from stats import get_num_words, count_occurance, sort_on, chars_dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath, "r") as file:
        return file.read()

#def main():
#    book_text = get_book_text("books/frankenstein.txt")
#    print(book_text)

#def main():
#    count = len(get_book_text("books/frankenstein.txt").split())
#    print(f"Found {count} total words")

#main()

#def main():
#    count = get_num_words(get_book_text("books/frankenstein.txt"))
#    print(f"Found {count} total words")

#main()

def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    words = get_num_words(text)
    counts = count_occurance(text)
    sorted_chars = chars_dict_to_sorted_list(counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()