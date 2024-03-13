from database import ClientText
# from api.routes import SupabaseRoutes
import requests
from api import headers
from datetime import datetime, timedelta


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

    # TODO: Need to create this when there is a live fixture
    @staticmethod
    def league_live_fixtures(league_id: int):
        try:
            live_params: {} = {'live': 'all', 'league': league_id}

            response = requests.get(ClientText.ENDPOINTS["leagues"]["fixtures"], headers=headers, params=live_params)
            data: {} = response.json()
            live_fixtures: {} = data["response"]

            if len(live_fixtures) == 0:
                return False

            live_matches = []
            for matches in live_fixtures:
                match_data = {
                    "kick-off": matches['fixture']['timestamp'],
                    "home": matches['teams']["home"]["name"],
                    "home_score": matches["goals"]["home"],
                    "time": matches['fixture']['status']["elapsed"],
                    "away": matches['teams']["away"]["name"],
                    "away_score": matches["goals"]["away"],
                    "events": []
                }

                for event in matches['events']:
                    if event["type"] == "Goal":
                        event_data = {
                            "elapsed": event['time']['elapsed'],
                            "player_name": event['player']['name']
                        }
                        match_data['events'].append(event_data)

                live_matches.append(match_data)

            return live_matches

        except Exception as e:
            print("Problem making API Call:", str(e))
            return None

    @staticmethod
    def league_upcoming_fixtures(league_id: int):
        try:
            current_date = datetime.now().date()
            next_7_days = [current_date + timedelta(days=i) for i in range(7)]
            current_year = datetime.now().year - 1
            end_date = next_7_days[-1]
            upcoming_params = {
                "league": league_id,
                "season": current_year,
                "from": current_date.strftime('%Y-%m-%d'),
                "to": end_date.strftime('%Y-%m-%d'),
                "timezone": "Europe/London"
            }

            response = requests.get(
                ClientText.ENDPOINTS["leagues"]["fixtures"], headers=headers, params=upcoming_params
            )

            data: {} = response.json()
            fixtures_data: {} = data["response"]
            upcoming_fixtures = []

            for fixture in fixtures_data:
                fixture_info = {
                    'date': fixture['fixture']["date"],
                    "home": fixture['teams']['home']['name'],
                    "away": fixture['teams']['away']['name'],
                    "time": fixture['fixture']['timestamp'],
                }

                upcoming_fixtures.append(fixture_info)

            return upcoming_fixtures

        except Exception as e:
            print("Problem making API Call:", str(e))
            return None
