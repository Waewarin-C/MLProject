class Player:
    
    used_symbols = set()

    def __init__(self, player_symbol, player_tag):

        if player_symbol is None or player_tag is None:
            raise ValueError("Player symbol and player tag must be provided.")

        if type(player_symbol) != str:
            raise ValueError("Invalid type for player symbol. Expected string.")

        if type(player_tag) != str:
            raise ValueError("Invalid type for player tag. Expected string.")

        if player_symbol in Player.used_symbols or player_symbol.lower() in Player.used_symbols:
            raise Exception("Symbol already in use.")

        self.player_symbol = player_symbol
        self.player_tag = player_tag

        Player.used_symbols.add(player_symbol)

    def get_player_symbol(self):
        return self.player_symbol

    def get_player_tag(self):
        return self.player_tag