import sys
from stats import get_char_counts, get_sorted_char_list, get_word_count


def validate_input():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(filepath: str) -> str:
    with open(filepath) as f:
        text = f.read()
        return text
    
def get_book_report(
        filepath: str,
        word_count: int,
        sorted_char_counts: list[dict]
    ) -> str:
    report = (
        f"============ BOOKBOT ============\n"
        f"Analyzing book found at {filepath}...\n"
        f"----------- Word Count ----------\n"
        f"Found {word_count} total words\n"
        f"--------- Character Count -------\n"
    )
    for count in sorted_char_counts:
        if count["char"].isalpha():
            report += f"{count['char']}: {count['num']}\n"
    report += "============= END ==============="
    return report


def main():
    validate_input()
    filepath = sys.argv[1]

    text = get_book_text(filepath)
    word_count = get_word_count(text)
    char_counts = get_char_counts(text)
    sorted_char_counts = get_sorted_char_list(char_counts)
    
    print(get_book_report(filepath, word_count, sorted_char_counts))


if __name__ == "__main__":
    main()
