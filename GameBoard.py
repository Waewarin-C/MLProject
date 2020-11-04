import numpy as np


def outOfBounds(coord):
    row, col = coord
    return row < 0 or row >= 3 or col < 0 or col >= 3


class GameBoard:

    def __init__(self):
        self.used_spaces = dict()
        self.board = np.full((3, 3), '.', dtype=str)
        self.size_range = range(0, 3)

    def isSpaceTaken(self, coord):
        '''
        Endpoint into the gameboard. If it's taken
        prevent an event from taking place;
        Player will need to choose another location.
        '''
        if coord in self.used_spaces:
            return True
        return False

    def setSpaceTaken(self, coord):
        '''
        Sets the coordinate of the game board as taken.
        Used to prevent overlap of choice.
        '''
        if type(coord) != tuple:
            raise ValueError("Invalid type for board space. Excepted tuple.")

        self.used_spaces[coord] = True

    def display_board(self):
        for row in self.size_range:
            for col in range(0, 2):
                print(self.board[row, col], end=' ')
            # Get around fencepost issue
            print(self.board[row, self.size_range.stop - 1])
        print()

    def placeSymbol(self, coord, player_symbol):
        row, col = coord
        self.board[row, col] = player_symbol
        self.setSpaceTaken(coord)
