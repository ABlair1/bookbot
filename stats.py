def get_word_count(text: str) -> int:
    return len(text.split())

def get_char_counts(text: str) -> dict:
    char_counts = {}
    for char in text:
        if char.lower() in char_counts:
            char_counts[char.lower()] += 1
        else:
            char_counts[char.lower()] = 1
    return char_counts

def get_sorted_char_list(char_counts: dict) -> list[dict]:
    counts_list = [{"char": c, "num": n} for c, n in char_counts.items()]
    counts_list.sort(reverse=True, key=lambda count: count["num"])
    return counts_list
