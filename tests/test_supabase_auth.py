import unittest
from unittest.mock import patch
from api.routes import SupabaseRoutes
from utils import Response

SUPABASE_PATH: str = 'database.supabase_utils.supabase'


class TestSupabaseUser(unittest.TestCase):
    @patch(SUPABASE_PATH)
    def test_check_user_success(self, mock_supabase):
        mock_supabase.table().select().eq().single().execute.return_value = ({'username': 'Tony'}, 1)

        result = SupabaseRoutes.check_user('Tony')
        username_result = result.message[1]

        self.assertTrue(result.success, "Call was successful")
        self.assertEqual(username_result, {'username': 'Tony'}, "Expected API Call to return {username: Tony}")

    @patch(SUPABASE_PATH)
    def test_check_user_failure(self, mock_supabase):
        mock_supabase.table().select().eq().single().execute.return_value = ({'username': 'Testing'}, 1)

        result = SupabaseRoutes.check_user("Testing")
        username_result = result.message

        self.assertFalse(result.success)
        self.assertEqual(username_result, "signup")

    @patch(SUPABASE_PATH)
    def test_supabase_down(self, mock_supabase):
        # Simulate Supabase being down by raising an exception
        mock_supabase.table().select().eq().single().execute.side_effect = Exception("Supabase is down")

        result = SupabaseRoutes.check_user("Testing")

        self.assertFalse(result.success)
        self.assertEqual(result.error_message, "")


class TestSupabasePassword(unittest.TestCase):
    @patch(SUPABASE_PATH)
    def test_check_password_success(self, mock_supabase):
        mock_supabase.table().select().eq().single().execute.return_value = ({'password': 'Testing!123'}, 1)

        result = SupabaseRoutes.check_password('Testing!123')
        username_result = result.message[1]

        self.assertTrue(result.success, "Call was successful")
        self.assertEqual(username_result, {'password': 'Testing!123'}, "Expected API Call to return {password: Tony}")

    @patch(SUPABASE_PATH)
    def test_check_password_failure(self, mock_supabase):
        mock_supabase.table().select().eq().single().execute.return_value = ({'password': 'Testing'}, 1)

        result = SupabaseRoutes.check_password("Testing")
        username_result = result.message

        self.assertFalse(result.success)
        self.assertEqual(username_result, "signup")


if __name__ == '__main__':
    unittest.main(verbosity=2)
