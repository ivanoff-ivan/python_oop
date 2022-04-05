class Guild:
    def __init__(self, name):
        self.name = name
        self.a_list_of_players = []

    def assign_player(self, player):  # Player
        if not player.guild == self.name and not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        elif player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        else:
            self.a_list_of_players.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        if player_name not in map(lambda x: x.name, self.a_list_of_players):
            return f"Player {player_name} is not in the guild."
        self.a_list_of_players.remove(next(filter(lambda x: x.name == player_name, self.a_list_of_players)))
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        data = f"Guild: {self.name}\n"
        for char in self.a_list_of_players:
            data += char.player_info()
        return data
