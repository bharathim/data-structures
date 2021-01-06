import unittest
from typing import List


def max_consecutive_ones(nums: List[int]) -> int:
    slow_index, fast_index, local_max, global_max = 0, 0, 0, 0

    while fast_index < len(nums):
        if nums[fast_index] == 0:
            global_max = max(global_max, local_max)
            slow_index = fast_index + 1

        fast_index += 1
        local_max = fast_index - slow_index

    return max(global_max, local_max)


class TestMaxConsecutiveOnes(unittest.TestCase):

    def test_max_consecutive_ones_empty(self):
        self.assertEqual(max_consecutive_ones([]), 0)

    def test_max_consecutive_ones_zero(self):
        self.assertEqual(max_consecutive_ones([0]), 0)

    def test_max_consecutive_ones_one(self):
        self.assertEqual(max_consecutive_ones([1]), 1)

    def test_max_consecutive_ones_one(self):
        self.assertEqual(max_consecutive_ones([0, 1]), 1)

    def test_max_consecutive_ones_one_zero(self):
        self.assertEqual(max_consecutive_ones([1, 0]), 1)

    def test_max_consecutive_ones_two_ones(self):
        self.assertEqual(max_consecutive_ones([1, 1]), 2)

    def test_max_consecutive_ones_ones_and_zeros(self):
        self.assertEqual(max_consecutive_ones([1, 1, 0, 1]), 2)

    def test_max_consecutive_ones_ones_and_zeros(self):
        self.assertEqual(max_consecutive_ones([1, 1, 0, 1, 1, 1]), 3)


if __name__ == '__main__':
    unittest.main()
