from typing import List
import re


class UserInputChecks:
    def __init__(self, username):
        self.username: str = username

    @staticmethod
    def input_affirmation(input_value: str) -> bool:
        valid_response: List[str] = ["y", "n", "yes", "no"]
        lowercase_value: str = input_value.lower()

        if lowercase_value in valid_response:
            return True

        return False

    @staticmethod
    def password_validation(password: str) -> bool:
        if len(password) < 8:
            return False

        if not re.search(r'[A-Z]', password):
            return False

        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False

        if ' ' in password:
            return False

        if not re.search(r'\d', password):
            return False

        return True
