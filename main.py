def char_stats(text):
    ltext = text.lower()
    r = {}
    for c in ltext:
        if c not in r:
            r[c] = 0
        r[c] += 1
    return r

def sort_on(item):
    return item["num"]

def process_stats(stats):
    ls = [{"key":k, "num":v} for k, v in stats.items()]
    ls.sort(reverse=True, key=sort_on)
    return ls

def main():
    book_file = "books/frankenstein.txt"
    with open(book_file) as f:
        file_contents = f.read()
        
        words = file_contents.split()
        word_n = len(words)

        stats = char_stats(file_contents)
        processed_stats = process_stats(stats)
        
        print(f"--- Begin report of {book_file} ---")
        print(f"{word_n} words found in the document")
        print()
        for item in processed_stats:
            c = item["key"]
            n = item["num"]
            if c.isalpha():
                print(f"The '{c}' character was found {n} times")
        print("--- End report ---")

main()
