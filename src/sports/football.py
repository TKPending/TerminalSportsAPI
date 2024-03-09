from api.clients import FootballClient

user = None


def handle_user_choices(username: str, chosen_option: str):
    global user

    user = FootballClient(username, chosen_option)

    if chosen_option == "saved":
        saved_settings()
        return
    elif chosen_option == "league":
        league_information()
        return
    elif chosen_option == "team":
        team_information()
        return
    elif chosen_option == "settings":
        settings()
        return

    return


def saved_settings():
    return


def league_information():
    user.rapid_leagues()
    return


def team_information():
    return


def settings():
    return
