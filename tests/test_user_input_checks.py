import unittest
from unittest.mock import patch
from utils import UserInputChecks

INPUT_PATH: str = 'utils.user_input_checks.UserInputChecks'


class TestUserInputs(unittest.TestCase):
    @patch(INPUT_PATH)
    def test_input_affirmation_valid_responses(self, mock_input_checks):
        mock_input_checks.input_affirmation.return_value = True

        result = UserInputChecks.input_affirmation("y")
        self.assertTrue(result)

        result = UserInputChecks.input_affirmation("n")
        self.assertTrue(result)

        result = UserInputChecks.input_affirmation("yes")
        self.assertTrue(result)

        result = UserInputChecks.input_affirmation("no")
        self.assertTrue(result)

    @patch(INPUT_PATH)
    def test_input_affirmation_invalid_responses(self, mock_input_checks):
        mock_input_checks.input_affirmation.return_value = False

        result = UserInputChecks.input_affirmation("invalid")
        self.assertFalse(result)

        result = UserInputChecks.input_affirmation("maybe")
        self.assertFalse(result)

    @patch(INPUT_PATH)
    def test_username_validation_valid(self, mock_input_checks):
        mock_input_checks.username_validation.return_value = True

        result = UserInputChecks.username_validation("valid_username")
        self.assertTrue(result)

    @patch(INPUT_PATH)
    def test_username_validation_invalid_length(self, mock_input_checks):
        mock_input_checks.username_validation.return_value = False

        result = UserInputChecks.username_validation("ab")
        self.assertFalse(result)

    @patch(INPUT_PATH)
    def test_username_validation_invalid_whitespace(self, mock_input_checks):
        mock_input_checks.username_validation.return_value = False

        result = UserInputChecks.username_validation("invalid username")
        self.assertFalse(result)

    @patch(INPUT_PATH)
    def test_password_validation_valid(self, mock_input_checks):
        mock_input_checks.password_validation.return_value = True

        result = UserInputChecks.password_validation("Valid@Password123")
        self.assertTrue(result)

    @patch(INPUT_PATH)
    def test_password_validation_invalid_length(self, mock_input_checks):
        mock_input_checks.password_validation.return_value = False

        result = UserInputChecks.password_validation("Short1")
        self.assertFalse(result)

    @patch(INPUT_PATH)
    def test_password_validation_missing_uppercase(self, mock_input_checks):
        mock_input_checks.password_validation.return_value = False

        result = UserInputChecks.password_validation("nouppercase123$")
        self.assertFalse(result)

    @patch(INPUT_PATH)
    def test_password_validation_missing_special_character(self, mock_input_checks):
        mock_input_checks.password_validation.return_value = False

        result = UserInputChecks.password_validation("MissingSpecialCharacter123")
        self.assertFalse(result)

    @patch(INPUT_PATH)
    def test_password_validation_invalid_whitespace(self, mock_input_checks):
        mock_input_checks.password_validation.return_value = False

        result = UserInputChecks.password_validation("Invalid Password with spaces")
        self.assertFalse(result)

    @patch(INPUT_PATH)
    def test_password_validation_missing_digit(self, mock_input_checks):
        mock_input_checks.password_validation.return_value = False

        result = UserInputChecks.password_validation("NoDigitSpecialCharacter$")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
