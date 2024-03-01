from typing import List

from project import player
from project.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players: List[Player] = []

    def assign_player(self, player: Player):
        if player in self.players:
            return f"Player {player} is already in the guild."
        if player != player.guild:
            return f"Player {player} is in another guild."

        self.players.append(player)
        player.guild = self.name

    def kick_player(self, player_name):
        if player_name not in self.players:
            return f"Player {player_name} is not in the guild."

        self.players.remove(player_name)
        player.guild = Player.DEFAULT_GUILD
        return f"Player {player_name} has been removed from the guild"

    def guild_info(self):
        result = f"Guild; {self.name}"

        for p in self.players:
            result += f"\n{p.player_info()}"

        return result