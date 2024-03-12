from api.clients import FootballClient
from .football_utils import match_teams, print_league
from utils import Response


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
    while True:
        print("Please enter the league and country:\n")
        league: str = input("League: ").lower()
        country: str = input("Country: ").lower()

        if league == "" or country == "":
            print("Can't find league without both League and Country\n")
            continue

        league_check: bool or {} = match_teams(league, country)

        if not league_check:
            print("Sorry! League doesn't exist or Currently unavailable")
            return

        rapid_league_id: int = league_check["league_id"]

        league_table: [{}] = FootballClient.league_table(league_id=rapid_league_id)

        # Fill DB with team id for fixtures

        print_league(league_table)


def team_information():
    return


def settings():
    return
