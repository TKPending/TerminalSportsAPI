from utils.cli_handler import CLIHandler
from utils.error_handler import ErrorHandler
from database.messages import ClientText


def main() -> None:
    username: str = CLIHandler.get_username()
    ErrorHandler.empty_string(username)

    # Check if user exists (Backend)

    password: str = CLIHandler.enter_password(ClientText.INTRODUCTION["password"]["first"], message=1)
    ErrorHandler.empty_string(password)

    # Depending on existence confirm password (Backend)

    password_check: bool = CLIHandler.confirm_password(existing_password=password)
    ErrorHandler.false_return(password_check)


if __name__ == '__main__':
    main()
