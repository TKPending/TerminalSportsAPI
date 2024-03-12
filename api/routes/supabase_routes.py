from database import supabase
from utils import Response


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
    def fetch_populate_league(leagues: [{}]):
        try:
            league_to_insert = [{
                "league_id": league.get('api_id', None),
                "league_name": league.get('league_name', None),
                "league_country": league.get("league_country", None)
            }
                for league in leagues]

            data, _count = supabase.table('leagues').upsert(league_to_insert).execute()

            print("\nSuccessfully uploaded to Supabase\n\n")
        except Exception as e:
            print(f"\nUnsuccessfully uploading to Supabase. Error: {str(e)}\n\n")
