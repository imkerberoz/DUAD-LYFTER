# test_sort_hyphenated_string.py
import unittest


def sort_hyphenated_string(text):
    words = text.split('-')
    words.sort()
    return '-'.join(words)


class TestSortHyphenatedString(unittest.TestCase):
    
    def test_example_from_exercise(self):
        input_str = "python-variable-funcion-computadora-monitor"
        expected = "computadora-funcion-monitor-python-variable"
        self.assertEqual(
            sort_hyphenated_string(input_str),
            expected,
            "Should sort alphabetically and keep hyphens"
        )

    def test_example_from_your_submission(self):
        input_str = "Zinc-York-Walter-Born-Apple-Frank"
        expected = "Apple-Born-Frank-Walter-York-Zinc"
        self.assertEqual(
            sort_hyphenated_string(input_str),
            expected,
            "Should sort example correctly (case-sensitive)"
        )

    def test_three_words_mixed_case(self):
        input_str = "Banana-Apple-Cherry"
        expected = "Apple-Banana-Cherry"
        self.assertEqual(
            sort_hyphenated_string(input_str),
            expected,
            "Should handle mixed case and sort correctly"
        )


if __name__ == '__main__':
    unittest.main()