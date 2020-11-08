from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
import tensorflow as tf
from TicTacToe import *
import numpy as np

#install these packages: tf-agents, gym

from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

tf.compat.v1.enable_v2_behavior()

# Let's make the assumption that the agent is always player 2.
class TrainingEnvironment(TicTacToe):

    def __init__(self):
        super.__init__(Player('X', 'Rand_Bot'), Player('O', 'Agent'))


