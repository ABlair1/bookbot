from stats import get_char_counts, get_word_count


filepath = "./books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    text = get_book_text(filepath)

    word_count = get_word_count(text)
    print(f"{word_count} words found in the document")

    character_counts = get_char_counts(text)
    print(character_counts)


main()
