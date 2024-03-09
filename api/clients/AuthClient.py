from api.routes import SupabaseRoutes
from database import ClientText
from utils import Response


class AuthClient:
    @staticmethod
    def check_user_exists(username: str) -> Response:
        response: Response = SupabaseRoutes.check_user(username)

        if response.success:
            data: any = response.message[1]["username"]

            if data == username:
                return Response(success=True)
        else:
            if response.message == "signup":
                return Response(success=False, message=ClientText.INTRODUCTION["signup"])
            else:
                return Response(success=False, message=ClientText.ERROR["supabase_connection"])

    @staticmethod
    def check_password(password: str):
        response: Response = SupabaseRoutes.check_password(password)

        if response.success:
            data: any = response.message[1]["password"]

            if data == password:
                return Response(success=True)
        else:
            if response.message == "signup":
                return Response(success=False, message=ClientText.INTRODUCTION["signup"])
            else:
                return Response(success=False, message=ClientText.ERROR["supabase_connection"])

    @staticmethod
    def create_user(username, password):
        try:
            response_data = SupabaseRoutes.create_user(username, password)

            if bool(response_data):
                return Response(success=True, message=ClientText.INTRODUCTION["account_creation"]["success"])
            else:
                return Response(success=False, message=ClientText.INTRODUCTION["account_creation"]["failure"])
        except Exception as e:
            print(f"\nLocation: AuthClient line 34: " + str(e))
            return Response(success=False, error_message=ClientText.ERROR["supabase_connection"])
