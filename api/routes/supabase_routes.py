from database import supabase


class SupabaseRoutes:
    @staticmethod
    def check_user(username: str):
        response = supabase.table('users').select('username').eq('username', username).single()

        return response

    @staticmethod
    def create_user(username: str, password: str):
        data, _ = supabase.table("users").insert({"username": username, "password": password}).execute()

        return data
