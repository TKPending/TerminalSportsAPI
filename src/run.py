from utils import CLIHandler, ErrorHandler
from .authentication.auth import authentication_flow
from .sports import sport_options


def run() -> None:
    username: str = CLIHandler.get_username()
    ErrorHandler.empty_string(username)

    authentication_flow(username)

    print(f"\nWelcome {username}\n")

    sport_options(username)
