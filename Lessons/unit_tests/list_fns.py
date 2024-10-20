"""Unit Test Practice."""


def get_first(input: list[str]) -> str:
    """Return first element."""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Remove first element."""
    input.pop(0)  # 0 indicates the first element/index to remove


def get_and_remove(input: list[str]) -> str:
    """Remove first element AND return it."""
    first_elem: str = input[0]
    input.pop(0)
    return first_elem  # Return needs to go after pop
