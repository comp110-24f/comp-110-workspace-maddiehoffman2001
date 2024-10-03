"""Mutating functions."""

__author__ = "730684336"


def manual_append(input: list[int], value: int) -> None:
    input.append(value)


def double(input: list[int]) -> None:
    index: int = 0
    while index < len(input):
        input[index] *= 2
        index += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_1)
print(list_1)
print(list_2)
