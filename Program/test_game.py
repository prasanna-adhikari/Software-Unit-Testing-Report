"""Test cases for the Number Guessing Game."""
import unittest
import random
from unittest.mock import patch
from game import generate_random_number, get_user_guess, provide_hints


class TestNumberGuessingGame(unittest.TestCase):
    """Test class for the Number Guessing Game."""

    def test_generate_random_number(self):
        """Test generate_random_number function."""
        random.seed(42)  # Set a random seed for reproducibility
        random_number = generate_random_number()
        self.assertEqual(random_number, [1, 0, 4, 9])

    @patch('builtins.input', side_effect=['1234'])
    def test_get_user_guess_valid_guess(self, _):
        """Test get_user_guess function with a valid guess."""
        self.assertEqual(get_user_guess(), [1, 2, 3, 4])

    @patch('builtins.input', side_effect=['q'])
    def test_get_user_guess_quit(self, _):
        """Test get_user_guess function when user quits."""
        self.assertIsNone(get_user_guess())

    @patch('builtins.input', side_effect=['123', 'q'])
    def test_get_user_guess_invalid_length(self, _):
        """Test get_user_guess function with an invalid length."""
        self.assertIsNone(get_user_guess())

    @patch('builtins.input', side_effect=['abcd', 'q'])
    def test_get_user_guess_non_digit_characters(self, _):
        """Test get_user_guess function with non-digit characters."""
        self.assertIsNone(get_user_guess())

    @patch('builtins.input', side_effect=['12ab', 'q'])
    def test_get_user_guess_mixed_input(self, _):
        """Test get_user_guess function with mixed input."""
        self.assertIsNone(get_user_guess())

    def test_provide_hints_all_correct(self):
        """Test provide_hints function when all digits are correct."""
        self.assertEqual(provide_hints("1234", "1234"), ["o", "o", "o", "o"])

    def test_provide_hints_none_correct(self):
        """Test provide_hints function when no digits are correct."""
        self.assertEqual(provide_hints("1234", "5678"), [" ", " ", " ", " "])

    def test_provide_hints_mixed_correct(self):
        """Test provide_hints function with mixed correct digits."""
        self.assertEqual(provide_hints("9872", "8822"), ["x", "o", "x", "o"])

    def test_provide_hints_correct_numbers_diff_position(self):
        """Test provide_hints function with correct
            digits in different positions."""
        self.assertEqual(provide_hints("1234", "4321"), ["x", "x", "x", "x"])


if __name__ == '__main__':
    unittest.main()
