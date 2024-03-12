from database import supabase
from utils import Response
from database import ClientText


class SupabaseRoutes:
    @staticmethod
    def check_user(username: str) -> Response:
        try:
            response_data, _ = supabase.table('users').select('username').eq('username', username).single().execute()

            return Response(success=True, message=response_data)
        except Exception as e:
            problem: str = str(e)

            if "0 rows" in problem:
                return Response(success=False, message="signup")
            else:
                return Response(success=False, error_message="failed")

    @staticmethod
    def check_password(password: str) -> Response:
        try:
            response_data, _ = supabase.table('users').select('password').eq('password', password).single().execute()

            return Response(success=True, message=response_data)
        except Exception as e:
            problem: str = str(e)

            if "0 rows" in problem:
                return Response(success=False, message="signup")
            else:
                return Response(success=False, error_message="failed")

    @staticmethod
    def create_user(username: str, password: str):
        data, _ = supabase.table("users").insert({"username": username, "password": password}).execute()

        return data

    @staticmethod
    def load_leagues() -> [{}]:
        try:
            data, _ = supabase.table("leagues").select("*").execute()

            return data
        except Exception as e:
            print(f"Error: {e}")
            print(ClientText.SUPABASE["failed_call"])

    @staticmethod
    def load_specific_leagues(league: str):
        try:
            data, _ = supabase.table("leagues").select("*").eq("league_country", league).execute()

            return data
        except Exception as e:
            print(f"Error: {e}")
            print(ClientText.SUPABASE["failed_call"])

    @staticmethod
    def fetch_populate_teams(league_table: [{}]):
        try:
            teams_to_insert = [{
                "team_id": team.get("team_id", None),
                "team_name": team.get("team", None)
            } for team in league_table]

            data, _ = supabase.table("teams").upsert(teams_to_insert).execute()

            print("League Found!")
        except Exception as e:
            print(f"\nTeams not found: {str(e)}\n\n")

    # ONE TIME USE
    @staticmethod
    def fetch_populate_league(leagues: [{}]) -> None:
        try:
            league_to_insert = [{
                "league_id": league.get('api_id', None),
                "league_name": league.get('league_name', None),
                "league_country": league.get("league_country", None)
            }
                for league in leagues]

            data, _ = supabase.table('leagues').upsert(league_to_insert).execute()

            print("\nSuccessfully uploaded to Supabase\n\n")
        except Exception as e:
            print(f"\nUnsuccessfully uploading to Supabase. Error: {str(e)}\n\n")
