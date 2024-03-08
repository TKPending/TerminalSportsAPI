from typing import List


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
