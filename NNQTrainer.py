import numpy as np
import tensorflow as tf
from Player import Player
from GameBoard import *
from QNet import *

action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                        3: (1, 0), 4: (1, 1), 5: (1, 2),
                        6: (2, 0), 7: (2, 1), 8: (2, 2)}

WINNING_REWARD = 1.0
TIE_REWARD = 0.5
LOSING_PENALTY = 0.0
REWARD_DISCOUNT = 0.95

SESSION = tf.compat.v1.Session()

class NNQTrainer(Player):

    def __int__(self, player_symbol, player_tag):
        super().__init__(player_symbol, player_tag)

        self.move_history = []
        self.board_position = []
        self.next_max = []
        self.values = []
        #self.name = name how does this work with this agent
        self.NN = QNet('QLearner')
        self.training = True

    def board_state_to_vector(self, boardState):
        player1 = []
        player2 = []
        empty = []

        for i in boardState:
            if i == 1:
                player1.append[i] = 1
                player2.append[i] = 0
                empty.append[i] = 0
            elif i == 2:
                player1.append[i] = 0
                player2.append[i] = 1
                empty.append[i] = 0
            elif i == 0:
                player1.append[i] = 0
                player2.append[i] = 0
                empty.append[i] = 1

        vector = np.array([player1, player2, empty])
        vector = vector.reshape(-1)
        return vector

    def move(self, board):
        print(board.get_board_state())
        state = []
        for i in board.get_board_state():
            state.append(i)
        self.board_position = state

        NN_input = self.board_state_to_vector(board.get_board_state())

        probs, qvalues = SESSION.run([self.NN.probabilities, self.NN.queueValues], feed_dict={self.NN.input_pos: [NN_input]})
        probabilities = probs[0]
        queue_values = qvalues[0]
        queue_values = np.copy(queue_values)

        for index, p in enumerate(queue_values):
            coord = action_to_coordinate(index)
            if not board.isSpaceTaken(coord):
                probabilities[index] = -1
        move = np.argmax(probabilities)

        if len(self.move_history) > 0:
            self.next_max.append(queue_values[move])

        self.move_history(move)
        self.values.append(queue_values)

        return move

    def calculate_targets(self):
        game_len = len(self.move_history)
        target_values = []
        for i in range(game_len):
            target = np.copy(self.values[i])
            target[self.move_history[i]] = REWARD_DISCOUNT * self.next_max[i]
            target_values.append(target)
        return target_values

    def result(self, gameResult):
        if gameResult is "won":
            final_value = WINNING_REWARD
        elif gameResult is "loss":
            final_value = LOSING_PENALTY
        elif gameResult is "tie":
            final_value = TIE_REWARD

        self.next_max.append(final_value)

        if self.training:
            targets = self.calculate_targets()
            NN_input = [self.board_state_to_vector(history) for history in self.board_position]
            SESSION.run([self.NN.train_step], feed_dict={self.NN.input_pos : NN_input, self.NN.input_target: targets})
