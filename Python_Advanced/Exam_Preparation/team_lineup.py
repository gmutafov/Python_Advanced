def team_lineup(*args):
    country_players = {}
    for player_name, country in args:
        if country not in country_players:
            country_players[country] = []
        country_players[country].append(player_name)

    result = ""

    sorted_teams = sorted(country_players.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for country, players in sorted_teams:
        result += f"{country}:\n"
        for player in players:
            result += f"  -{player}\n"

    return result[:-1]


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany")))
