from api.routes import SupabaseRoutes
from utils import CLIHandler
from prettytable import PrettyTable


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
