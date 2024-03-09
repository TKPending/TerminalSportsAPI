from api.routes import SupabaseRoutes
from database import ClientText
from utils import Response


class AuthClient:
    @staticmethod
    def check_user_exists(username: str) -> Response:
        try:
            response = SupabaseRoutes.check_user(username)

            if response is not None:
                data = response.json
                if isinstance(data, dict) and bool(data):
                    return Response(success=True)
                else:
                    return Response(success=False, message=ClientText.INTRODUCTION["signup"])
            else:
                return Response(success=False, message=ClientText.ERROR["supabase_connection"])
        except Exception as e:
            print(f"\nLocation: AuthClient line 21: " + str(e))
            return Response(success=False, error_message=ClientText.ERROR["supabase_connection"])

    @staticmethod
    def create_user(username, password):
        try:
            response_data = SupabaseRoutes.create_user(username, password)

            if bool(response_data):
                return Response(success=True, message=ClientText.INTRODUCTION["account_creation"]["success"])
            else:
                return Response(succuess=False, message=ClientText.INTRODUCTION["account_creation"]["failure"])
        except Exception as e:
            print(f"\nLocation: AuthClient line 34: " + str(e))
            return Response(success=False, error_message=ClientText.ERROR["supabase_connection"])
