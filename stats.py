def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_counts = {}
    for character in text:
        lower_character = character.lower()
        if lower_character in character_counts:
            character_counts[lower_character] += 1
        else:
            character_counts[lower_character] = 1
    return character_counts

def sort_on(character):
    return character["num"]

def sort_counts(dictionary):
    character_list = []
    for character in dictionary:
        character_list.append({"char": character, "num": dictionary[character]})
    character_list.sort(reverse=True, key=sort_on)
    return character_list