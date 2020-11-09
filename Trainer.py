from TrainingEnvironment import *
from random import *

NUM_EPISODES = 1_000

class Trainer:

    def __init__(self):

        self.environment = TrainingEnvironment()
        self.tf_env = tf_py_environment.TFPyEnvironment(self.environment)


    # Note: If the current player is NOT the agent, it must move randomly and THEN we can
    # allow the agent to play. Below are the methods we can use to make this happen:
    #
    #       if not self.environment._is_agent_current_player() then
    #           self.environment._play_random_non_agent()
    #
    def begin_training(self):
        pass


    # From here we can define functions that create whatever kind of agent we want and send it into the
    # training environment.


    # possible TODO if it even shows up
    def visualize(self):
        pass

