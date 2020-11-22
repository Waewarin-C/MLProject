from GameEnvironment import *
from GameBoard import *
from random import *

NUM_EPISODES = 1_000

LOSING_PENALTY = 0
WINNING_REWARD = 1
TIE_REWARD = 0.5

LEARNING_RATE = 0.9     # alpha
DISCOUNT_FACTOR = 0.95   # gamma
Q_INITIALIZER = 0.5

STATES = dict()
Q_TABLE = []

# TODO: find a way to save the trained agent

class Trainer:

    def __init__(self):
        self.environment = GameEnvironment()
        self.tf_env = tf_py_environment.TFPyEnvironment(self.environment)

        self.board = GameBoard()
        Q_TABLE = [[Q_INITIALIZER for i in range(9)]]   # store it in one dimension
        STATES[1] = Q_TABLE

    def move(self):
        pass

    def finished(self):
        #reverse the move history
        #loop through the move history
        #calculate the q table values based on this history using the tabular calculation



    # From here we can define whatever kind of agent creation we want.

    # possible TODO if it even shows up
    def visualize(self):
        pass
