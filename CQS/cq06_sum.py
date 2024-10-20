"""Summing the elements of a list using different loops"""

__author__ = "730684336"


def w_sum(vals: list[float]) -> float:
    """Return Sum Using a While Loop"""
    index: int = 0
    total: float = 0.0
    while index < len(vals):
        total += vals[index]
        index += 1
    return total


def f_sum(vals: list[float]) -> float:
    """Return Sum Using a For Loop"""
    total: float = 0.0
    for elem in vals:
        total += elem
    return total


def f_range_sum(vals: list[float]) -> float:
    """Return Sum Using a For...In Range...Loop"""
    total: float = 0.0
    for elem in range(len(vals)):
        total += vals[elem]
    return total

