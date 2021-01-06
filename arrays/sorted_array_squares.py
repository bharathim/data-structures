import unittest
from typing import List


def sorted_array_squares(nums: List[int]) -> List[int]:
    start = 0
    end = len(nums) - 1
    result = [None] * len(nums)

    for i in reversed(range(len(nums))):
        if abs(nums[start]) < abs(nums[end]):
            square = nums[end] * nums[end]
            end -= 1
        else:
            square = nums[start] * nums[start]
            start += 1
        result[i] = square
    return result


class TestSortedArraySquares(unittest.TestCase):
    def test_sorted_array_squares(self):
        self.assertEqual(sorted_array_squares([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])

    def test_sorted_array_squares(self):
        self.assertEqual(sorted_array_squares([-7, -3, 2, 3, 11]), [4, 9, 9, 49, 121])
