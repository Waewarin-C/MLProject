from typing import Dict, Tuple
import GameEnvironment
from GameBoard import *
from tf_agents.environments import tf_py_environment
from random import *

from Player import Player

NUM_EPISODES = 1_000

LEARNING_RATE = 0.9  # alpha
DISCOUNT_FACTOR = 0.95  # gamma
Q_INITIALIZER = 0.5

# The states should be the key into the dict. The value should be the columns of Q values. (in this case 9)
# Board provides a "get_board_state()" function now, that should allow you to index by state.
action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                        3: (1, 0), 4: (1, 1), 5: (1, 2),
                        6: (2, 0), 7: (2, 1), 8: (2, 2)}


# TODO: find a way to save the trained agent

class TabularTrainer(Player):

    def __init__(self, player_symbol, player_tag):
        self.environment = GameEnvironment.GameEnvironment()
        self.tf_env = tf_py_environment.TFPyEnvironment(self.environment)
        # TODO: One row for every state, one column for every action. The dict will obtain a new one
        # THERE ARE 255_168 states possible.
        self.player_symbol = player_symbol
        self.player_tag = player_tag
        self.queue = {}
        self.playHistory = []

    def move(self, board) -> int:
        boardState = board.get_board_state()
        queueValues = np.empty([0, 9])

        if boardState in self.queue:
            queueValues = self.queue[boardState]
        else:
            queueValues = [Q_INITIALIZER for i in range(9)]
            self.queue[boardState] = queueValues
        while True:
            move = np.argmax(queueValues)
            coord = action_to_coordinate[move]
            max = np.max(queueValues)
            if max == -1:
                return max
            if board.isSpaceTaken(coord):
                queueValues[move] = -1.0
            else:
                self.playHistory.append((board.get_board_state(), move))
                return move

    def result(self):
        pass
        # reverse the move history
        # loop through the move history
        # calculate the q table values based on this history using the tabular calculation

    # From here we can define whatever kind of agent creation we want.

    # possible TODO if it even shows up
    def visualize(self):
        pass
