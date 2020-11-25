import GameEnvironment
from GameBoard import *
from tf_agents.environments import tf_py_environment
from random import *

NUM_EPISODES = 1_000

LOSING_PENALTY = 0
WINNING_REWARD = 1
TIE_REWARD = 0.5

LEARNING_RATE = 0.9     # alpha
DISCOUNT_FACTOR = 0.95   # gamma
Q_INITIALIZER = 0.5

# The states should be the key into the dict. The value should be the columns of Q values. (in this case 9)
# Board provides a "get_board_state()" function now, that should allow you to index by state.
STATES = dict()
Q_TABLE = []

# TODO: find a way to save the trained agent

class TabularTrainer:

    def __init__(self):
        self.environment = GameEnvironment.GameEnvironment()
        self.tf_env = tf_py_environment.TFPyEnvironment(self.environment)

        self.board = GameBoard()
        # TODO: One row for every state, one column for every action. The dict will obtain a new one
        # THERE ARE 255_168 states possible.
        Q_TABLE = [Q_INITIALIZER for _ in range(9)]
        STATES[1] = Q_TABLE

    def move(self):
        pass

    def finished(self):
        pass
        #reverse the move history
        #loop through the move history
        #calculate the q table values based on this history using the tabular calculation



    # From here we can define whatever kind of agent creation we want.

    # possible TODO if it even shows up
    def visualize(self):
        pass
