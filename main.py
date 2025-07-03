from stats import count_words, count_characters, sort_counts

def get_book_test(filepath):
    with open(filepath) as f:
        contents = f.read()
    return contents

def main():
    filepath = "books/frankenstein.txt"
    text = get_book_test(filepath)
    word_count = count_words(text)
    character_counts = count_characters(text)
    sorted_counts = sort_counts(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in sorted_counts:
        if character["char"].isalpha():
            print(f"{character["char"]}: {character["num"]}")
    print("============= END ===============")

main()