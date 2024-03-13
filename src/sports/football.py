from api.clients import FootballClient
from .football_utils import match_teams, print_league, print_upcoming_fixtures
from api.routes import SupabaseRoutes
from utils import CLIHandler


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


def league_information() -> None:
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

        SupabaseRoutes.fetch_populate_teams(league_table)

        print_league(league_table)

        if not league_fixtures(league_id=rapid_league_id):
            break


def league_fixtures(league_id: int) -> None:
    count: int = 0
    while True:
        if count > 3:
            return False

        fixture: str = input(
            "\nLive Fixtures [live] or Upcoming Fixtures [upcoming] or Return [R] or Close [C]\n"
        ).lower()

        if fixture == "c":
            CLIHandler.close_program()
        elif fixture == "r":
            return False
        elif fixture == "live":
            live_fixtures = FootballClient.league_live_fixtures(league_id)

            if not live_fixtures:
                print("\nThere are currently no live matches")
                return False
        elif fixture == "upcoming":
            upcoming_fixture = FootballClient.league_upcoming_fixtures(league_id)

            print_upcoming_fixtures(upcoming_fixture)
            return

        print("Invalid input, please enter the correct response!\n")
        count += 1


def team_information():
    return


def settings():
    return
