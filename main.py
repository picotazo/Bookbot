import sys
from stats import count_words, count_letters, sort_characters, count_specific_word


def get_book_text(filepath):
    """Return the full text of the requested book."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    # Validate CLI arguments
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    # Use the provided book path
    book_path = sys.argv[1]

    # Load the book text
    book_text = get_book_text(book_path)

    # Count words
    num_words = count_words(book_text)
    print(f"Found {num_words} total words")

    # Count characters
    char_counts = count_letters(book_text)

    # Sort characters by frequency
    sorted_chars = sort_characters(char_counts)

    # Print character counts
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()





