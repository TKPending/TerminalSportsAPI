class ClientText:
    INTRODUCTION = {
        "welcome": "Welcome to Terminal Sport API",
        "username": "Please enter username: ",
        "password": {
            "first": "Please enter password: ",
            "second": "Confirm Password: "
        }
    }

    WARNING = {
        "username": "\nUsername must be more than 3 letters, and not include spaces \n",
        "password": "\nPassword must have a capital letter, special character, number, more than 3 letters "
                    "and not include spaces \n",
        "confirm_password": "\nPassword doesn't match\n"
    }

    ERROR = {
        "empty_string": "\nERROR: Value entered was empty.",
        "force_close": "\nERROR: Closing application\n"
    }
