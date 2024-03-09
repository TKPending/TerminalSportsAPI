import unittest
from unittest.mock import patch
from utils.user_input_checks import UserInputChecks
from utils.cli_handler import CLIHandler
from database.messages import ClientText


class TestCLIHandler(unittest.TestCase):
    @patch('builtins.input', side_effect=["ValidUsername"])
    def test_get_username_valid(self, mock_input):
        result = CLIHandler.get_username()
        self.assertEqual(result, "ValidUsername")

    @patch('builtins.input', side_effect=["Invalid User", "Another Invalid User", "ValidUsername"])
    def test_get_username_invalid_then_valid(self, mock_input):
        result = CLIHandler.get_username()
        self.assertEqual(result, "ValidUsername")

    # TODO: Need to fix this test
    # @patch('builtins.input', side_effect=["ValidPassword123-", "ValidPassword123-"])
    # def test_confirm_password_matching(self, mock_input):
    #     result = CLIHandler.confirm_password("ValidPassword123")
    #     self.assertTrue(result)
    #
    # @patch('builtins.input', side_effect=["ValidPassword123"])
    # def test_enter_password_valid(self, mock_input):
    #     result = CLIHandler.enter_password("Enter Password: ", message=1)
    #     self.assertEqual(result, "ValidPassword123")

    @patch('builtins.input', side_effect=["InvalidPassword", "AnotherInvalidPassword", "ValidPassword123"])
    def test_enter_password_invalid_then_valid(self, mock_input):
        result = CLIHandler.enter_password("Enter Password: ", message=1)
        self.assertEqual(result, "")

    @patch('builtins.input', side_effect=["ValidPassword123", "MismatchedPassword", "MismatchedPassword"])
    def test_confirm_password_not_matching(self, mock_input):
        result = CLIHandler.confirm_password("ValidPassword123")
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main(verbosity=2)
