from Player import *
from GameBoard import *


class TicTacToe:

    def __init__(self, player_one, player_two):

        if player_one is None or player_two is None:
            raise ValueError("Players must be provided.")

        if type(player_one) != Player or type(player_two) != Player:
            raise ValueError("Players must be of the Player class.")

        self.current_player_index = 0;

        self.player_one = player_one
        self.player_two = player_two

        self.player_queue = list()
        self.player_queue.append(player_one)
        self.player_queue.append(player_two)
        self.num_players = len(self.player_queue)

        self.game_board = GameBoard()

        Player.used_symbols.clear()

    def play_round(self, coord):
        current_player = self.get_current_player()
        self.game_board.placeSymbol(coord, current_player.getPlayerSymbol())
        self.current_player_index = (self.current_player_index + 1) % self.num_players

    def get_current_player(self):
        return self.player_queue[self.current_player_index]

    def get_board(self):
        return self.game_board

    def get_current_player_tag(self):
        return self.get_current_player().player_tag

    def isValidMove(self, coord):
        return not self.game_board.isSpaceTaken(coord) and not outOfBounds(coord)
