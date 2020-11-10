from GameEnvironment import *
from random import *

NUM_EPISODES = 1_000


class Trainer:

    def __init__(self):
        self.environment = GameEnvironment()
        self.tf_env = tf_py_environment.TFPyEnvironment(self.environment)

    def begin_training(self):
        pass

    # From here we can define whatever kind of agent creation we want.

    # possible TODO if it even shows up
    def visualize(self):
        pass
