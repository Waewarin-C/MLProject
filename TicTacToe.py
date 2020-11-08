from Player import *
from GameBoard import *


# This class is representative of the tic tac toe game itself.
class TicTacToe:

    def __init__(self, player_one, player_two):

        if player_one is None or player_two is None:
            raise ValueError("Players must be provided.")

        if type(player_one) != Player or type(player_two) != Player:
            raise ValueError("Players must be of the Player class.")

        self.current_player_index = 0;

        self.player_one = player_one
        self.player_two = player_two

        self.symbol_numbers = {player_one.get_player_symbol() : 1, player_two.get_player_symbol() : 2}

        self.player_queue = list()
        self.player_queue.append(player_one)
        self.player_queue.append(player_two)
        self.num_players = len(self.player_queue)

        self.game_board = GameBoard(default_spaces=0)

        self.winning_player = None
        self.game_won = False
        self.tie_game = False

        Player.used_symbols.clear()

    def play_round(self, coord):
        current_player = self.get_current_player()

        symbol = self.symbol_numbers[current_player.get_player_symbol()]

        self.game_board.placeSymbol(coord, symbol)
        self.current_player_index = (self.current_player_index + 1) % self.num_players

    def get_current_player(self):
        return self.player_queue[self.current_player_index]

    def get_board(self):
        return self.game_board

    def get_current_player_tag(self):
        return self.get_current_player().player_tag

    def isValidMove(self, coord):
        return not self.game_board.isSpaceTaken(coord) and not outOfBounds(coord)

    def get_winning_player(self):
        return self.winning_player

    def determine_winner(self):

        top_horizontal_band = self.game_board.get_horizontal_band_top()
        middle_horizontal_band = self.game_board.get_horizontal_band_middle()
        bottom_horizontal_band = self.game_board.get_horizontal_band_bottom()

        left_vertical_band = self.game_board.get_vertical_band_left()
        middle_vertical_band = self.game_board.get_vertical_band_middle()
        right_vertical_band = self.game_board.get_vertical_band_right()

        top_left_diagonal = self.game_board.get_diagonal_band_from_top_left()
        top_right_diagonal = self.game_board.get_diagonal_band_from_top_right()

        board_bands = list()
        board_bands.append(top_horizontal_band)
        board_bands.append(middle_horizontal_band)
        board_bands.append(bottom_horizontal_band)
        board_bands.append(top_left_diagonal)
        board_bands.append(top_right_diagonal)
        board_bands.append(left_vertical_band)
        board_bands.append(middle_vertical_band)
        board_bands.append(right_vertical_band)

        for band in board_bands:
            print(band)
            self.check_band_for_consecutive_elements(band)
            if self.game_won:
                return

        self.check_bands_for_tie(board_bands)


    def check_band_for_consecutive_elements(self, band):

        symbol = self.symbol_numbers[self.player_one.get_player_symbol()]

        if self.band_has_consecutive_elements(band):
            if band[0] == symbol:
                self.winning_player = self.player_one
            else:
                self.winning_player = self.player_two
            self.game_won = True


    def check_bands_for_tie(self, bands):

        for band in bands:
            for element in band:
                if element == self.game_board.default_spaces:
                    self.tie_game = False
                    return

        self.tie_game = True

    def band_has_consecutive_elements(self, band):

        element_index = 0
        previous = band[element_index]

        if previous == self.game_board.default_spaces:
            return False

        element_index += 1
        while element_index < 3:

            if band[element_index] == self.game_board.default_spaces:
                return False

            if band[element_index] != previous:
                return False

            previous = band[element_index]

            element_index += 1

        return True
