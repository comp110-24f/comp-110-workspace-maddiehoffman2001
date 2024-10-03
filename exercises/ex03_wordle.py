"""EX03 - Wordle Game"""

__author__ = "730684336"


def main(secret: str) -> None:
    """This is the entrypoint of the program."""
    turns: int = 1
    max_turns: int = 6
    while turns <= max_turns:
        print(f"=== Turn {turns}/{max_turns} ===")
        guess = input_guess(len(secret))
        print(emojified(guess=guess, secret=secret))

        if guess == secret:
            print(f"You won in {turns}/{max_turns}!")
            turns = 7
            # 7 causes the while loop to become false and it will end the game / loop
        elif turns == 6:
            print(f"X/{max_turns} - Sorry, try again tomorrow!")
        turns += 1
        # Once they reach turn #6, they cannot submit another word


def input_guess(secret_word_len: int) -> str:
    """Prompting user to guess word with correct length"""
    player_word: str = input(f"Enter a {secret_word_len} character word: ")
    while len(player_word) != secret_word_len:
        player_word = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return player_word


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Searching for Instances of Charactrer in Secret Word"""
    assert len(char_guess) == 1
    index: int = 0
    while index < len(secret_word):
        if char_guess == secret_word[index]:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Comparing Player Word and Secret Word and Returning Emojis"""
    assert len(guess) == len(secret)
    # caller is expected to put in word of correct length
    index: int = 0
    box: str = ""
    # box variable allows you to concatenate emojis
    while index < len(secret):
        if guess[index] == secret[index]:
            index += 1
            box += GREEN_BOX
        else:
            present: bool = contains_char(secret, guess[index])
            if present:
                index += 1
                box += YELLOW_BOX
            else:
                index += 1
                box += WHITE_BOX
    return box


# Box Colors Returned
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
WHITE_BOX: str = "\U00002B1C"

if __name__ == "__main__":
    main(secret="codes")
# Having this allows you to change the secret word only from one spot
# This makes it easy to make changes
