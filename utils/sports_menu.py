from database import ClientText
from utils import Response


class SportsMenu:
    def __init__(self):
        pass

    @staticmethod
    def display_options(sport: str) -> Response:
        count = 0

        while True:
            initial_choice: str = input(ClientText.MENU["home"][sport]).lower()

            if initial_choice not in ClientText.MENU["options"][sport] and count > 3:
                print(ClientText.MENU["failed_options"])
                return Response(success=False, message=ClientText.MENU["failed_options"])
            elif initial_choice in ClientText.MENU["options"][sport]:
                return Response(success=True, message=initial_choice)

