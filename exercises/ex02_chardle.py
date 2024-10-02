"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730684336"


def main() -> None:
    """Required for creating entry point of Chardle game"""
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    """Requires user to input a 5 letter word."""
    word: str = input("Enter a 5-character word:")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
        # exit is put here to exit the program due to error
    else:
        return word


def input_letter() -> str:
    """Requires user to input a letter"""
    letter: str = input("Enter a single character:")
    if len(letter) != 1:
        print("Error: Character must be a single character.")
        exit()
        # exit must come after the print so that the program still prints error
    else:
        return letter
        # do not have else statement print anything in this case


def contains_char(word: str, letter: str) -> None:
    """Determining number of instances of letter in word."""
    count: int = 0
    # introduce count as varible to figure out number of letter instances
    print("Searching for " + letter + " in " + word)
    if word[0] == letter:
        count = 1 + count
        # "count ="" must come first, having 1 + count = count did not work
        # must identify variable first
        print(letter + " found at index 0")
        # don't forget to add space after "
    if word[1] == letter:
        count = 1 + count
        print(letter + " found at index 1")
    if word[2] == letter:
        count = 1 + count
        print(letter + " found at index 2")
    if word[3] == letter:
        count = 1 + count
        print(letter + " found at index 3")
    if word[4] == letter:
        count = 1 + count
        print(letter + " found at index 4")
    if count == 0:
        print(" No instances of " + letter + " found in " + word)
    if count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    if count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)


# in REPL (contains_char(word= input_word, letter= input_letter))

if __name__ == "__main__":
    main()
