"""ex04 List Utility Functions."""

__author__ = "730684336"


def all(input: list[int], value: int) -> bool:
    """Figuring out if value matches all numbers in input."""
    index: int = 0
    if len(input) == 0:
        return False
    # if list is empty, the code should return false
    # empty list is []
    while index < len(input):
        if input[index] != value:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Determining the max in the set of numbers."""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    current_max: int = input[0]
    # Current max shoud just take the first index as the first max
    # Need current max to update when the code encounters higher number
    while index < len(input):
        if input[index] > current_max:
            current_max = input[index]
            # current max will take the new value if code enters if block
        index += 1
    return current_max


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Determining if input 1 is equal to input 2."""
    index: int = 0
    if len(input1) != len(input2):
        # we cannot assume input1 and input2 have the same length
        return False
    while index < len(input1):
        if input1[index] != input2[index]:
            return False
        index += 1
    return True


def extend(input1: list[int], input2: list[int]) -> None:
    """Mutating input 1 by adding input 2 to the end of it."""
    index: int = 0
    while index < len(input2):
        input1.append(input2[index])
        # append addds items to the list
        # cannot append all of input2 at once, need to add by 1 integer
        # use index function to iterate through all integers of input2
        index += 1
