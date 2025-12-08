import sys
from stats import count_words, lower_case, build_char_list, sort_on

def get_book_text(filepath):
    with open(filepath) as f:
        the_book = f.read()
        return the_book

def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    numbers = count_words(text)
    letters = lower_case(text)
    chars = build_char_list(letters)
    chars.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {numbers} total words")
    print("--------- Character Count -------")
    for item in chars:
        ch = item["char"]
        if ch.isalpha():
            print(f"{ch}: {item['num']}")

    print("============= END ===============")

main()
