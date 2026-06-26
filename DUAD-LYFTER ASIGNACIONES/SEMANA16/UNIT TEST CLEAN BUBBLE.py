import unittest
import random

def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        for j in range(n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
    return my_list


class TestBubbleSort(unittest.TestCase):

    def test_small_list(self):
        data = [64, 34, 25, 12, 22, 11, 90]
        expected = [11, 12, 22, 25, 34, 64, 90]
        bubble_sort(data)
        self.assertEqual(data, expected)

    def test_large_list(self):
        data = [random.randint(-500, 500) for _ in range(150)]
        original_copy = data.copy()
        bubble_sort(data)
        self.assertEqual(data, sorted(original_copy))

    def test_empty_list(self):
        data = []
        bubble_sort(data)
        self.assertEqual(data, [])

    def test_non_list_parameters(self):
        invalid_inputs = [
            123,
            3.14159,
            "hello world",
            True,
            None,
            (1, 2, 3),
            {"name": "test", "age": 25},
        ]
        for bad_value in invalid_inputs:
            with self.assertRaises(TypeError):
                bubble_sort(bad_value)


if __name__ == '__main__':
    unittest.main()