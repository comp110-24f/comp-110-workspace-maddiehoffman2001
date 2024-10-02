"""Practicing my conditionals."""


def less_than_10(num: int) -> None:
    """Tell us if num < 10."""
    if num < 10:
        print("Small number!")  # then block
    else:
        print("Big number!")
    print("this is the end of the function!")


less_than_10(num=2)


def check_first_letter(word: str, letter: str) -> None:
    """Checks if letter is first character of word."""
    # return type is none because you aren't returning anything, just printing
    if word[0] == letter:  # need [0] to pull first letter of the "word"
        print("match!")
    else:
        print("no match!")


# if and else should be at the same indentation

check_first_letter(word="happy", letter="h")
check_first_letter(word="happy", letter="s")
