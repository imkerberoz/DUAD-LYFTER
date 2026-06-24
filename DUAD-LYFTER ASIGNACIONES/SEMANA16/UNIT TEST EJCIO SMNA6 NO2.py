# test_reverse_word.py
import unittest


def reverse_word(word):
    """
    Returns the given string reversed.
    
    Example:
    reverse_word("Hola mundo") → "odnum aloH"
    """
    return word[::-1]


class TestReverseWord(unittest.TestCase):
    
    def test_example_from_the_exercise(self):
        self.assertEqual(
            reverse_word("Hola mundo"),
            "odnum aloH",
            '"Hola mundo" reversed should be "odnum aloH"'
        )

    def test_simple_english_word(self):
        self.assertEqual(
            reverse_word("Hello"),
            "olleH",
            '"Hello" reversed should be "olleH"'
        )

    def test_word_with_punctuation_and_spaces(self):
        self.assertEqual(
            reverse_word("¡Hola, qué tal!"),
            "!lat éuq ,aloH¡",
            '"¡Hola, qué tal!" reversed should be "!lat éuq ,aloH¡"'
        )


if __name__ == '__main__':
    unittest.main()