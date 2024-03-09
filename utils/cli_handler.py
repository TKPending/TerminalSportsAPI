from utils.user_input_checks import UserInputChecks
from database.messages import ClientText


class CLIHandler:
    def __init__(self):
        pass

    @staticmethod
    def get_username() -> str:
        print(ClientText.INTRODUCTION["welcome"])
        count: int = 0

        while True:
            if count >= 3:
                return ""

            username: str = input(ClientText.INTRODUCTION["username"])
            username_check: bool = UserInputChecks.username_validation(username)

            if username_check:
                return username

            print(ClientText.WARNING["username"])
            count += 1

    @staticmethod
    def enter_password(password_text: str, message: int) -> str:
        count: int = 0

        while True:
            if count >= 3:
                return ""

            password: str = input(password_text)
            password_check: bool = UserInputChecks.password_validation(password)

            if password_check:
                return password

            print(ClientText.WARNING["invalid_password"])
            print(ClientText.WARNING["password"] if message == 1 else ClientText.WARNING["confirm_password"])
            count += 1

    @staticmethod
    def confirm_password(existing_password: str):
        second_password: str = CLIHandler.enter_password(ClientText.INTRODUCTION["password"]["second"], message=2)

        if existing_password != second_password:
            return False

        return True

    @staticmethod
    def choose_sport() -> bool:
        if UserInputChecks is None:
            return False

        print("Currently only Football is available.")
        user_input: str = input("Please enter Yes (Y) or No (N), if you understand: ")

        user_input_check: bool = UserInputChecks.input_affirmation(input_value=user_input)
        return user_input_check
