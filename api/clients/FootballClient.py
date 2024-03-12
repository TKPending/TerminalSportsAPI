# from utils import Response, ErrorHandler
from database import ClientText
# from api.routes import SupabaseRoutes
import requests
from api import headers


class FootballClient:
    def __init__(self, username: str, chosen_option: str):
        self.username = username
        self.chosen_option = chosen_option

    @staticmethod
    def rapid_leagues() -> [{}]:
        try:
            response = requests.get(ClientText.ENDPOINTS["leagues"]["football"], headers=headers)

            data: {} = response.json()
            leagues: [{}] = data["response"]

            all_leagues: [{}] = []

            for league in leagues:
                organised_result: {} = {
                    "api_id": league["league"]["id"],
                    "league_name": league["league"]["name"],
                    "league_country": league["country"]["name"]
                }

                all_leagues.append(organised_result)

            return all_leagues

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            print(ClientText.ENDPOINTS["default_error"])
            print("\n\n")
            return []
