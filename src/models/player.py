class Player():
    def __init__(self, name: str, game_id: int, player_id: int, role: str) -> None:
        self.name = name
        self.game_id = game_id
        self.player_id = player_id
        self.role = role