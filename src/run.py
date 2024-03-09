from utils import CLIHandler, ErrorHandler
from .authentication.auth import authentication_flow


def run() -> None:
    username: str = CLIHandler.get_username()
    ErrorHandler.empty_string(username)

    authentication_flow(username)
