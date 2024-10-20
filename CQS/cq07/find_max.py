"""cq07 - find_max"""

__author__ = "730684336"


def find_and_remove_max(input: list[int]) -> int:
    """Finds and removes the maximum number in a list."""
    if len(input) == 0:
        return -1
    idx: int = 0
    current_max: int = input[0]
    for num in input:
        if num > current_max:
            current_max = num
    while idx < len(input):
        if input[idx] == current_max:
            input.pop(idx)
        else:
            idx += 1
    return current_max
