from utils import Response
from database import ClientText
from api.routes import SupabaseRoutes
import requests
from api import headers


class FootballClient:
    def __init__(self, username: str, chosen_option: str):
        self.username = username
        self.chosen_option = chosen_option

    @staticmethod
    def rapid_leagues():
        response = requests.get(ClientText.ENDPOINTS["leagues"]["football"], headers=headers)

        data = response.json()
        print(data)

        # for leagues in data:=
        #     league_id = leagues["league"]["id"]
        #     league_name = leagues["league"]["name"]
        #     league_country = leagues["country"]["name"]
        #
        #     print(f"ID: {league_id} - League: {league_name} - Country: {league_country}")
