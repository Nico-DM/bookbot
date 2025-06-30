def get_book_test(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def count_words(text):
    words = text.split()
    return len(words)

def main():
    text = get_book_test("books/frankenstein.txt")
    word_count = count_words(text)
    print(f"{word_count} words found in the document")

main()