from user_input_checks import UserInputChecks


class CLIHandler:
    def __init__(self):
        self.UserInputChecks = None

    @staticmethod
    def get_username(self) -> None:
        print("Welcome to Terminal Client API!")
        username: str = input("Please enter username: ")

        self.UserInputChecks = UserInputChecks(username)

    @staticmethod
    def enter_password(self) -> str:
        password: str = input("Enter Password: ")

        return password

    @staticmethod
    def confirm_password(self):
        password: str = input("Please enter password: ")
        password_check: bool = self.UserInputChecks.password_validation(password=password)

        return password_check

    @staticmethod
    def choose_sport(self) -> bool:
        if self.UserInputChecks is None:
            return False

        print("Currently only Football is available.")
        user_input: str = input("Please enter Yes (Y) or No (N), if you understand: ")

        user_input_check: bool = self.UserInputChecks.input_affirmation(input_value=user_input)
        return user_input_check

    @staticmethod
    def football_redirection() -> None:
        return
