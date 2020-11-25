from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import abc
from typing import Any

import tensorflow as tf
from tf_agents.typing import types

from random import *
from TicTacToe import *
import numpy as np

# install these packages: tf-agents, gym

from tf_agents.environments import py_environment
from tf_agents.environments import tf_environment
from tf_agents.environments import tf_py_environment
from tf_agents.environments import utils
from tf_agents.specs import array_spec
from tf_agents.environments import wrappers
from tf_agents.environments import suite_gym
from tf_agents.trajectories import time_step as ts

from Training import LOSING_PENALTY, WINNING_REWARD, TIE_REWARD

tf.compat.v1.enable_v2_behavior()

'''
    Observation: an environment-specific object representing board state in the game.
    
    Reward: the amount of reward achieved by the previous action. 
    
    Done: returns a boolean response based on various scenarios. For example, perhaps the pole tipped too far, or you lost your last life.)
    
    Info: diagnostic information useful for debugging. 
    It can sometimes be useful for learning (for example, it might contain the raw probabilities behind the environment’s last state change).

'''

class GameEnvironment(py_environment.PyEnvironment):
    # For every action the agent chooses from 0 to 8, then this will provide the coordinate into the board.
    action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                            3: (1, 0), 4: (1, 1), 5: (1, 2),
                            6: (2, 0), 7: (2, 1), 8: (2, 2)}

    def __init__(self, custom_game=None):
        # One episode = One game round
        self._episode_ended = False

        if custom_game is None: # This condition is a consideration for training.
            self.game = TicTacToe(Player('O', 'Player 1'), Player('X', 'Agent'))
        else:
            self.game = custom_game

        self._state = self.game.get_board_grid()

        self._action_spec = array_spec.BoundedArraySpec(
            shape=(), dtype=np.int32, minimum=0, maximum=8, name='action')

        # Can be used to see what is or is not taken (0 = not taken).
        self._observation_spec = array_spec.BoundedArraySpec(
            shape=(3,3), dtype=self._state.dtype, minimum=0, maximum=2, name='observation')


    def observation_spec(self):
        return self._observation_spec

    def action_spec(self):
        return self._action_spec

    def _step(self, action: types.NestedArray) -> ts.TimeStep:

        action_coord = GameEnvironment.action_to_coordinate[int(action)]

        if self._episode_ended:
            # The last action ended the episode. Ignore the current action and start
            # a new episode.
            return self.reset()

        # Want it to make the right choice instead of choosing taken spot
        if self._is_spot_taken(action_coord):
            self._episode_ended = True
            return ts.termination(np.array(self._state, dtype=self._state.dtype), LOSING_PENALTY)

        if self.game.game_won and self.game.get_winning_player().player_tag == 'Agent':
            self._episode_ended = True
            return ts.termination(np.array(self._state, dtype=self._state.dtype), WINNING_REWARD)

        if self.game.game_won and not self.game.get_winning_player().player_tag == 'Agent':
            self._episode_ended = True
            return ts.termination(np.array(self._state, dtype=self._state.dtype), LOSING_PENALTY)

        if self.game.tie_game:
            self._episode_ended = True
            return ts.termination(np.array(self._state, dtype=self._state.dtype), TIE_REWARD)

        self.game.play_round(action_coord)
        self.game.determine_winner()

        return ts.transition(np.array(self._state, dtype=self._state.dtype), reward=INTERMEDIATE_REWARD, discount=DISCOUNT_FACTOR)

    def _reset(self):
        self.game = TicTacToe(Player('O', 'Player 1'), Player('X', 'Agent'))
        self._state = self.game.get_board_grid()
        self._episode_ended = False
        return ts.restart(np.array(self._state, dtype=self._state.dtype))

    # Auxilliary helper functions just in case it's needed...

    def _is_spot_taken(self, action_coord):
        return self.game.get_board().isSpaceTaken(action_coord)

    def _is_agent_current_player(self):
        return self.game.get_current_player_tag() == 'Agent'

    def _play_random_non_agent(self):

        choice = randrange(1,10)
        while not self.game.isValidMove(GameEnvironment.action_to_coordinate(choice)):
            choice = randrange(1, 10)

        self.game.play_round(choice)
        self.game.determine_winner()

    def display_current_state(self):
        self.game.game_board.display_board()