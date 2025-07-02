from stats import count_words, count_characters

def get_book_test(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    text = get_book_test("books/frankenstein.txt")
    word_count = count_words(text)
    character_counts = count_characters(text)
    print(f"{word_count} words found in the document")
    print(character_counts)

main()