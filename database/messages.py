class ClientText:
    INTRODUCTION = {
        "welcome": "Welcome to Terminal Sport API",
        "username": "Please enter username: ",
        "password": {
            "first": "Please enter password: ",
            "second": "Confirm Password: ",
            "incorrect": "Incorrect Password! Try again."
        },
        "signup": "\nCouldn't find user, please sign up\n",
        "account_creation": {
            "success": "\nYour account has been created!",
            "failure": "\nFailure creating account. Try again!\n"
        },
    }

    ENDPOINTS = {
        "leagues": {
            "football": "https://api-football-v1.p.rapidapi.com/v3/leagues",
            "league_table": "https://api-football-v1.p.rapidapi.com/v3/standings",
        },
        "default_error": "Problem making API Call"
    }

    SUPABASE = {
        "failed_call": "Failed request with Supabase."
    }

    MENU = {
        "options": {
            "football": ["saved", "league", "teams", "settings"]
        },
        "home": {
            "football": "\nMake A Choice\n\nSaved - League - Teams - Settings\n\n"
        },
        "failed_options": "\nFailed to choose a valid option\n"
    }

    SPORTS = {
        "available_sports": "Current Available Sports: Football",
        "choose_sport": "Choose a sport: ",
        "failed_chosen": "\nFailed to pick a sport!\n"
    }

    WARNING = {
        "username": "\nUsername must be more than 3 letters, and not include spaces \n",
        "password": "\nPassword must have a capital letter, special character, number, more than 3 letters "
                    "and not include spaces \n",
        "confirm_password": "\nPassword doesn't match\n",
        "invalid_password": "\nIncorrect Password! Try Again\n"
    }

    ERROR = {
        "empty_string": "\nERROR: Value entered was empty.",
        "force_close": "\nERROR: Closing application\n",
        "supabase_connection": "\nERROR: Problem connecting to DB\n"
    }
