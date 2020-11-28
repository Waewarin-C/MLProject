from GameBoard import *
from Player import Player

NUM_EPISODES = 1_000

LEARNING_RATE = 0.9  # alpha
DISCOUNT_FACTOR = 0.95  # gamma

Q_INITIALIZER = 0.5

WINNING_REWARD = 1.0
TIE_REWARD = 0.5
LOSING_PENALTY = 0.0

# The states should be the key into the dict. The value should be the columns of Q values. (in this case 9)
# Board provides a "get_board_state()" function now, that should allow you to index by state.
action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                        3: (1, 0), 4: (1, 1), 5: (1, 2),
                        6: (2, 0), 7: (2, 1), 8: (2, 2)}

class TabularTrainer(Player):

    def __init__(self, player_symbol, player_tag):
        super().__init__(player_symbol, player_tag)

        self.queue = {}
        self.playHistory = []

        self.final_q_values = np.empty([0, 9])

    def move(self, board) -> int:
        boardState = board.get_board_state()
        queueValues = self.get_state_q_values(boardState)

        while True:
            move = np.argmax(queueValues)
            coord = action_to_coordinate[move]

            max = np.max(queueValues)
            if max == -1.0:
                return max

            if board.isSpaceTaken(coord):
                queueValues[move] = -1.0
            else:
                self.playHistory.append((board.get_board_state(), move))
                return move

    # We will build the Q table in a lazy way
    # So we will only add the state when it is the first time it is seen
    def get_state_q_values(self, boardState) -> np.ndarray:
        queueValues = np.empty([0, 9])

        if boardState in self.queue:
            queueValues = self.queue[boardState]
        else:
            queueValues = [Q_INITIALIZER for i in range(9)]
            self.queue[boardState] = queueValues

        return queueValues

    def result(self, gameResult) -> np.ndarray:
        if gameResult is "won":
            final_value = WINNING_REWARD
        elif gameResult is "loss":
            final_value = LOSING_PENALTY
        elif gameResult is "tie":
            final_value = TIE_REWARD

        # Must reverse the play history because we will be working backwards
        self.playHistory.reverse()
        next_max_value = -1.0

        for history in self.playHistory:
            self.final_q_values = self.get_state_q_values(history[0])

            if next_max_value < 0:  # This will be the first time through the loop
                # The final step taken is the step that made the agent win, lose, or tie
                # so it will get the value that corresponds to the its winning status
                self.final_q_values[history[1]] = final_value
            else:
                # Work backwards to get the actual (or rather appropriate q values)
                # for each step further and further away from the final step
                # The q value for each state/step will decrease each time as it becomes
                # less important it is to the agent winning the game the further back we go
                # thus the use of the learning rate and the discount factor
                self.final_q_values[history[1]] = self.final_q_values[history[1]] * (1.0 - LEARNING_RATE) + LEARNING_RATE * DISCOUNT_FACTOR * next_max_value

            next_max_value = max(self.final_q_values)

    # possible TODO if it even shows up
    def visualize(self):
        pass
