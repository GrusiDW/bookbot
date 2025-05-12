def count_words (content):
    return len(content.split())

def count_characters (content):
    content = content.lower()
    character_dictionary = {}
    for character in content:
        if character not in character_dictionary:
            character_dictionary[character] = 1
        else:
            character_dictionary[character] += 1
    return character_dictionary

def sort_on(dict):
    return dict["num"]

def sorted_dict (character_count):
    sorted_list = []
    i = 0
    for character in character_count:
        char_dict = {"char": character, "num": character_count[character]}
        sorted_list.append(char_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list