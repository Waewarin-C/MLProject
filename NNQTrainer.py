import numpy as np
import tensorflow as tf
from Player import Player
from GameBoard import *
from QNet import *

WINNING_REWARD = 1.0
TIE_REWARD = 0.5
LOSING_PENALTY = 0.0

SESSION = None

class NNQTrainer(Player):

    def __int__(self, player_symbol, player_tag):
        super().__init__(player_symbol, player_tag)
        self.board_history = []
        self.move_history = []
        self.next_max = []
        self.values = []
        #self.name = name how does this work with this agent
        self.NN = QNet(player_tag)
        self.training = True

    def board_state_to_vector(self, boardState):
        print("board state to vector")

    def move(self):
        print('move')

    def calculate_targets(self):
        print('target')

    def result(self, gameResult):
        if gameResult is "won":
            final_value = WINNING_REWARD
        elif gameResult is "loss":
            final_value = LOSING_PENALTY
        elif gameResult is "tie":
            final_value = TIE_REWARD

        self.next_max.append(final_value)

        if self.training:
            self.calculate_targets()
            NN_input = [self.board_state_to_vector(history) for history in self.board_history]
            if SESSION is None:
                SESSION = tf.Session()
            SESSION.run([self.NN.train_step],feed_dict={self.NN.input_pos})
