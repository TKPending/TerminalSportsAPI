from database import ClientText
from utils import Response, ErrorHandler, SportsMenu
from api.clients import FootballClient


def sport_options(username: str) -> None:
    print(ClientText.SPORTS["available_sports"])
    chosen_sport: Response = choose_option()

    if not chosen_sport.success:
        ErrorHandler.default_exit(ClientText.ERROR["force_close"])

    while True:
        menu_option: Response = SportsMenu.display_options(sport=chosen_sport.message)

        if not menu_option.success:
            ErrorHandler.default_exit(ClientText.ERROR["force_close"])

        handle_menu_option(username=username, sport=chosen_sport.message, menu_option=menu_option.message)


def choose_option() -> Response:
    sports: [str] = ["football"]
    count: int = 0

    while True:
        if count > 3:
            return Response(success=False, message=ClientText.SPORTS["failed_chosen"])

        chosen_sport = input(ClientText.SPORTS["choose_sport"]).lower()

        if chosen_sport in sports:
            return Response(success=True, message=chosen_sport)

        count += 1


def handle_menu_option(username: str, sport: str, menu_option: str) -> None:
    if sport == "football":
        user = FootballClient(username, chosen_option=menu_option)

