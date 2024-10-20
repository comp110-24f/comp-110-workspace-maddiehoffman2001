"""ex05- List Unit Tests."""

__author__ = "730684336"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only even numbers from list."""
    evens: list[int] = []  # start with empty list and append as you find even nums
    for num in nums:
        if num % 2 == 0:
            # modulo function checks if num is divisible by 2
            evens.append(num)
    return evens


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Generates a list of numbers between start and end."""
    new_list: list[int] = []  # start with empty list and append as you go
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)
    if len(input) == 0 or start >= len(input) or end <= 0:
        # can use or function or seperate into seperate "if" functions
        return []
    for num in range(start, end):
        # for/in range/ function checks for nums within start and end idx
        new_list.append(input[num])
    return new_list


def add_at_index(input: list[int], elem: int, idx: int) -> None:
    """Place new element at index in list."""
    if idx > len(input) or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
    input.append(0)  # add space at the end of the list
    for x in range(len(input) - 1, idx, -1):
        input[x] = input[x - 1]  # shifts everything to the right
    input[idx] = elem  # new elem goes at open spot
