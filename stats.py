def count_words(text):
    words = text.split()
    return len(words)

def lower_case(text):
    char_count = {}
    cases = text.lower()
    for i in cases:
        if i in char_count:
            char_count[i] = char_count[i] + 1
        else:
            char_count[i] = 1
    return char_count 

def build_char_list(char_count):
    empty = []
    for char, count in char_count.items():
        empty.append({"char": char, "num": count})
    return empty

def sort_on(item):
    return item["num"]
