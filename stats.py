def count_words(text):
    """returns the number of words in the given text."""
    words = text.split()
    return len(words)

def count_letters(text):
    """returns a dictionary of character counts in the given text."""
    chars = {}
    for ch in text.lower():
        if ch in chars:
            chars[ch] += 1
        else:
            chars[ch] = 1
    return chars

def sort_characters(char_counts):
    """
    Convert the character-count dictionary into a sorted list of dictionaries.
    Each item looks like: {"char": "a", "num": 1234}
    Only alphabetical characters are included.
    Sorted from highest count to lowest.
    """
    sorted_list = []

    # Build the list of {"char": x, "num": y}
    for ch, count in char_counts.items():
        if ch.isalpha():  # skip non-letters
            sorted_list.append({"char": ch, "num": count})

    # Helper function for sorting
    def sort_key(item):
        return item["num"]

    # Sort descending by count
    sorted_list.sort(key=sort_key, reverse=True)
    return sorted_list

def count_specific_word(text, target):
    """Return how many times a specific word appears in the text."""
    words = text.lower().split()
    target = target.lower()
    count = 0

    for w in words:
        # Strip punctuation from the edges of the word
        w = w.strip(".,!?;:\"'()[]{}")
        if w == target:
            count += 1

    return count


