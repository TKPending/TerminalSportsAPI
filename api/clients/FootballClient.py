from utils import Response
from database import ClientText
from api.routes import SupabaseRoutes


class FootballClient:
    def __init__(self, username: str, chosen_option: str):
        self.username = username
        self.chosen_option = chosen_option

    def handle_user(self):
        if self.chosen_option == "saved":
            return
        elif self.chosen_option == "league":
            return
        elif self.chosen_option == "team":
            return
        elif self.chosen_option == "settings":
            return

        return

    def saved_settings(self):
        return

    def league_information(self):
        return

    def team_information(self):
        return

    def settings(self):
        return
