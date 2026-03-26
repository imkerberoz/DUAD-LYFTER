# test_get_primes.py
import unittest


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_primes(numbers):
    primes = []
    for num in numbers:
        if is_prime(num):
            primes.append(num)
    return primes


class TestGetPrimes(unittest.TestCase):
    
    def test_example_from_exercise(self):
        input_list = [1, 4, 6, 7, 13, 9, 67]
        expected = [7, 13, 67]
        self.assertEqual(
            get_primes(input_list),
            expected,
            "Should return [7, 13, 67] from [1, 4, 6, 7, 13, 9, 67]"
        )

    def test_your_original_test_list(self):
        input_list = [4, 55, 81, 66, 44, 20, 9, 7, 62, 114, 55, 68, 17, 3]
        expected = [7, 17, 3]
        self.assertEqual(
            get_primes(input_list),
            expected,
            "Should correctly identify 7, 17, and 3 as primes"
        )

    def test_list_with_small_primes_and_non_primes(self):
        input_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 1, 0, -5]
        expected = [2, 3, 5, 7, 11]
        self.assertEqual(
            get_primes(input_list),
            expected,
            "Should return all small primes: [2, 3, 5, 7, 11]"
        )


if __name__ == '__main__':
    unittest.main()