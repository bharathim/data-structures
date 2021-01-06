import unittest
from typing import List


def check_even_digits(n: int) -> bool:
    count = 0
    while n:
        n = n // 10
        count += 1

    return not(count & 1)


def find_numbers_with_even_number_of_digits(nums: List[int]) -> int:
    result = 0
    for n in nums:
        if check_even_digits(n):
            result += 1
    return result


class TestFindNumbers(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(find_numbers_with_even_number_of_digits([]), 0)

    def test_single_odd(self):
        self.assertEqual(find_numbers_with_even_number_of_digits([1]), 0)

    def test_single_even(self):
        self.assertEqual(find_numbers_with_even_number_of_digits([10]), 1)

    def test_double_even(self):
        self.assertEqual(find_numbers_with_even_number_of_digits([10, 1111]), 2)

    def test_double_odd(self):
        self.assertEqual(find_numbers_with_even_number_of_digits([1, 101]), 0)

    def test_mix(self):
        self.assertEqual(find_numbers_with_even_number_of_digits([1, 101, 2, 2222]), 1)


if __name__ == '__main__':
    unittest.main()
