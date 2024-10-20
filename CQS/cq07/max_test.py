from CQs.cq07.find_max import find_and_remove_max

"""cq07 - max_test"""

__author__ = "730684336"


def test_find_max() -> None:
    """Test that function finds the maximum and returns it."""
    nums: list[int] = [1, 2, 4, 8, 9]
    assert find_and_remove_max(nums) == 9


def test_remove_max() -> None:
    """Test that function returns mutated list."""
    nums: list[int] = [1, 2, 4, 8, 8]
    assert find_and_remove_max(nums) == 8
    assert nums == [1, 2, 4]


def test_empty_list() -> None:
    """Test that function returns correct value for empty list []."""
    nums: list[int] = []
    assert find_and_remove_max(nums) == -1
