# test_sum_of_list_unittest.py

import unittest


def sum_of_list(numbers):
    return sum(numbers)


class TestSumOfList(unittest.TestCase):

    def test_example_from_the_exercise(self):
        self.assertEqual(sum_of_list([4, 6, 2, 29]), 41, "4 + 6 + 2 + 29 should be 41")

    def test_positive_numbers_medium_size(self):
        self.assertEqual(sum_of_list([10, 20, 30, 40, 50]),150,"10 + 20 + 30 + 40 + 50 should be 150")

    def test_mixed_positive_and_negative_that_sums_to_zero(self):
        self.assertEqual(sum_of_list([-15, -5, 7, 13]),0,"-15 + -5 + 7 + 13 should equal 0")


if __name__ == '__main__':
    unittest.main()