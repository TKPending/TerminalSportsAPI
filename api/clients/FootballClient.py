# from utils import Response, ErrorHandler
from database import ClientText
# from api.routes import SupabaseRoutes
import requests
from api import headers
from datetime import datetime


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

    @staticmethod
    def league_table(league_id: int) -> [{}]:
        try:
            current_year = datetime.now().year - 1
            params: {} = {"season": current_year, "league": league_id}
            response = requests.get(ClientText.ENDPOINTS["leagues"]["league_table"], headers=headers, params=params)

            data: {} = response.json()
            league_table_data: {} = data["response"][0]["league"]["standings"][0]

            team_details: [{}] = []
            for team_data in league_table_data:
                team_info = {
                    'team_id': team_data['team']['id'],
                    'ranking': team_data['rank'],
                    'team': team_data['team']['name'],
                    'points': team_data['points'],
                    'played': team_data['all']['played'],
                    'wins': team_data['all']['win'],
                    'losses': team_data['all']['lose'],
                    'draw': team_data['all']['draw'],
                    'gd': team_data['goalsDiff'],
                    'gf': team_data['all']['goals']['for'],
                    'performance': team_data['form']
                }
                team_details.append(team_info)

            return team_details
        except Exception as e:
            print("Problem making API Call:", str(e))
            return None
