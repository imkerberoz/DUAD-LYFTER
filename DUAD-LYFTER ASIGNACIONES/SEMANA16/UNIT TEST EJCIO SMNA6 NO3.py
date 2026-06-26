# test_count_case_letters.py
import unittest
from io import StringIO
import sys


def count_case_letters(input_string):
    upper_count = 0
    lower_count = 0
    
    for char in input_string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
            
    print(f"There’s {upper_count} upper cases and {lower_count} lower cases")


class TestCountCaseLetters(unittest.TestCase):
    
    def capture_print(self, func, arg):
        captured = StringIO()
        old_stdout = sys.stdout
        sys.stdout = captured
        func(arg)
        sys.stdout = old_stdout
        return captured.getvalue().strip()

    def test_example_from_exercise(self):
        output = self.capture_print(count_case_letters, "I love Nación Sushi")
        self.assertEqual(
            output,
            "There’s 3 upper cases and 13 lower cases"
        )

    def test_mixed_case_and_non_letters(self):
        output = self.capture_print(count_case_letters, "I am tRyInG mY reaLly beST")
        self.assertEqual(
            output,
            "There’s 5 upper cases and 18 lower cases"
        )

    def test_only_upper_and_lower_no_other_chars(self):
        output = self.capture_print(count_case_letters, "PYTHONisGREAT")
        self.assertEqual(
            output,
            "There’s 6 upper cases and 6 lower cases"
        )


if __name__ == '__main__':
    unittest.main()