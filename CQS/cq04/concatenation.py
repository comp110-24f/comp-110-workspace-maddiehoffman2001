"""Importing and Concatination."""

__author__ = "730684336"


def concat(word1: str, word2: str) -> str:
    """Returns the concatination of two input strings"""
    return word1 + word2


word1: str = "happy"
word2: str = "tuesday"

if __name__ == "__main__":
    print(concat(word1, word2))
