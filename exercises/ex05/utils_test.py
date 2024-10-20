from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest

"""ex05 - 'list' Utility Functions Unit Tests"""

__author__ = "730684336"


def test_only_evens() -> None:
    """Test that function finds only even numbers."""
    nums: list[int] = [4, 6, 7, 8, 8, 9]
    assert only_evens(nums) == [4, 6, 8, 8]


def test_sub() -> None:
    """Test that function generates list at a subset of input list."""
    list1: list[int] = [10, 30, 70, 80, 90]
    assert sub(list1, 2, 5) == [70, 80, 90]


def test_add_at_index_raises_indexerror():
    """Test that function raises an IndexError when invalid index entered."""
    with pytest.raises(IndexError):
        add_at_index([4, 4, 6, 7], 8, 8)
