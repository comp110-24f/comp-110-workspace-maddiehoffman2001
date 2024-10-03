"""ex04 - List Utility Functions."""

__author__ = "730684336"


def all(input: list[int], value: int) -> bool:
    """Figuring out if value matches all numbers in input."""
    index: int = 0
    if len(input) == 0:
        return False
    while index < len(input):
        if input[index] != value:
            return False
        index += 1
    return True


def max(input: list[int]) -> int:
    """Determining the max in the set of numbers"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    index: int = 0
    current_max: int = input[0]
    while index < len(input):
        if input[index] > current_max:
            current_max = input[index]
        index += 1
    return current_max


def is_equal(input1: list[int], input2: list[int]) -> bool:
    """Determining if input 1 is equal to input 2"""
    index: int = 0
    if len(input1) != len(input2):
        return False
    while index < len(input1):
        if input1[index] != input2[index]:
            return False
        index += 1
    return True


def extend(input1: list[int], input2: list[int]) -> None:
    """Mutating input 1 by adding input 2 to the end of it"""
    index: int = 0
    while index < len(input2):
        input1.append(input2[index])
        index += 1
