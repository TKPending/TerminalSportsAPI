from utils import CLIHandler, ErrorHandler, Response
from api.clients import AuthClient
from database import ClientText


class PasswordType:
    def __init__(self, stage: str = "", password: str = ""):
        self.stage = stage
        self.password = password


def authentication_flow(username: str):
    user_exists: Response = AuthClient.check_user_exists(username)

    password: PasswordType = password_process(user_exists)

    if password.stage == "signup":
        account_creation(username, password.password)
    elif password.stage == "failed":
        ErrorHandler.default_exit("Failed Sign in / up Process")

    return


def password_process(user_exists: Response) -> PasswordType:
    if not user_exists.success:
        if user_exists.error_message:
            ErrorHandler.default_exit(user_exists.error_message)
        else:
            print(user_exists.message)

    password: str = CLIHandler.enter_password(ClientText.INTRODUCTION["password"]["first"], message=1)
    ErrorHandler.empty_string(password)

    # New User
    if not user_exists.success:
        password_check: bool = CLIHandler.confirm_password(existing_password=password)
        ErrorHandler.false_return(password_check)
        return PasswordType(stage="signup", password=password)
    else:
        # Existing User
        password_check: Response = AuthClient.check_password(password)

        if password_check.success:
            return PasswordType(stage="signin", password=password)
        elif password_check.message:
            return password_process(user_exists)

        return PasswordType(stage="failed")


def account_creation(username: str, password: str):
    account_creation_status: Response = AuthClient.create_user(username, password)

    if account_creation_status.success:
        return
    else:
        if account_creation_status.message:
            ErrorHandler.default_exit(account_creation_status.message)
        else:
            ErrorHandler.default_exit(account_creation_status.error_message)
