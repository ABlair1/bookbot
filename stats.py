def get_word_count(text):
    word_count = len(text.split())
    return word_count

def get_char_counts(text):
    char_counts = {}
    for char in text:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
        else:
            char_counts[char.lower()] = 1
    return char_counts
