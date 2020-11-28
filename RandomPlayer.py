from GameBoard import *
from Player import Player
import random

action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                        3: (1, 0), 4: (1, 1), 5: (1, 2),
                        6: (2, 0), 7: (2, 1), 8: (2, 2)}

class RandomPlayer(Player):

    def __init__(self, player_symbol, player_tag):
        super().__init__(player_symbol, player_tag)

    def move(self, board) -> int:
        boardState = board.get_board_state()

        check = False
        for i in boardState:
            if i == '0':
                check = True
        if check is False:
            return -1

        while True:
            move = random.randint(0,8)
            coord = action_to_coordinate[move]

            if board.isSpaceTaken(coord):
                pass
            else:
                return move