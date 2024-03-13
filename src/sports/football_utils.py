from api.routes import SupabaseRoutes
from utils import CLIHandler
from prettytable import PrettyTable
from datetime import datetime


def match_teams(league: str, country: str) -> bool:
    response: () = SupabaseRoutes.load_specific_leagues(country.capitalize())
    country_data: [{}] = response[1]
    CLIHandler.loading("leagues...")

    for leagues in country_data:
        if leagues["league_name"].lower() == league:
            return leagues

    return False


def print_league(league_table: [{}]) -> None:
    if league_table is None:
        print("Error retrieving league data.")
        return

    table = PrettyTable()

    table.field_names = ["Rank", "Team", "Played", "Points", "Wins", "Draws", "Losses", "GF", "GD", "Performance"]

    for team in league_table:
        table.add_row([
            team['ranking'],
            team['team'],
            team['played'],
            team['points'],
            team["wins"],
            team['draw'],
            team["losses"],
            team['gf'],
            team["gd"],
            team['performance']
        ])

    print(table)


def print_upcoming_fixtures(upcoming_fixtures: [{}]) -> None:
    if upcoming_fixtures is None:
        print("Error retrieving fixture data")

    table = PrettyTable()

    table.field_names = ["Date", "Home", "vs", "Away", "Time"]

    for fixture in upcoming_fixtures:
        fixture_date = datetime.utcfromtimestamp(fixture['time'])
        formatted_date = fixture_date.strftime('%d-%m-%Y')
        formatted_time = fixture_date.strftime('%H:%M')

        table.add_row([
            formatted_date,
            fixture['home'],
            "vs",
            fixture['away'],
            formatted_time,
        ])

    print(table)
