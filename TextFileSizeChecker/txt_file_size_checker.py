import sys


def analyze_text(filename=sys.argv[1]):
    """Calculate the number of lines, words and characters in a file

    Args:
        filename: The name of the file to analyze.

    Raises:
        IOError: If 'filename' does not exist or can't be read.

    Returns:
        A tuple where the first element is the number of lines in
        the file, the second element is the number of words and the
        third element is the number of characters.
    """
    lines = 0
    words = 0
    characters = 0
    with open(filename, "rt") as f:
        for line in f:
            lines += 1
            words += len(line.split())
            characters += len(line)
    print(f"\nTotal number of lines in a text file is {lines}\n")
    print(f"Total number of words in a text file is {words}\n")
    print(f"Total number of characters in a text file is {characters}\n")


if __name__ == '__main__':
    analyze_text()
