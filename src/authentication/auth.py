from utils import CLIHandler, ErrorHandler, Response
from api.clients import AuthClient
from database import ClientText


def authentication_flow(username: str):
    user_exists: Response = AuthClient.check_user_exists(username)

    password: str = account_signup(user_exists)
    account_creation(username, password)


def account_signup(user_exists: Response) -> str:
    if not user_exists.success:
        if user_exists.error_message:
            ErrorHandler.default_exit(user_exists.error_message)
        else:
            print(user_exists.message)

    password: str = CLIHandler.enter_password(ClientText.INTRODUCTION["password"]["first"], message=1)
    ErrorHandler.empty_string(password)

    if not user_exists.success:
        password_check: bool = CLIHandler.confirm_password(existing_password=password)
        ErrorHandler.false_return(password_check)

    return password


def account_creation(username: str, password: str):
    account_creation_status: Response = AuthClient.create_user(username, password)

    if account_creation_status.success:
        return
    else:
        if account_creation_status.message:
            ErrorHandler.default_exit(account_creation_status.message)
        else:
            ErrorHandler.default_exit(account_creation_status.error_message)
