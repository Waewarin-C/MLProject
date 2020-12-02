from GameBoard import *
from Player import Player
import random
import os

filepath = os.path.join('.\Data', 'qtable.txt')

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
        self.historic_data = self.load_to_dict()

    def move_agent(self, board) -> int:
        boardState = board.get_board_state()
        if boardState in self.historic_data:
            queueValues = self.historic_data[boardState]
            while True:
                move = np.argmax(queueValues)
                coord = action_to_coordinate[move]

                max = np.max(queueValues)
                if max == -1.0:
                    return max

                if board.isSpaceTaken(coord):
                    queueValues[move] = -1.0
                else:
                    return move
        else:
            check = False
            for i in boardState:
                if i == '0':
                    check = True
            if check is False:
                return -1

            while True:
                move = random.randint(0, 8)
                coord = action_to_coordinate[move]
                if board.isSpaceTaken(coord):
                  pass
                else:
                    return move



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

        if (boardState in self.historic_data) and (len(self.historic_data) != 0):
            queueValues = self.historic_data[boardState]
        else:
            queueValues = [Q_INITIALIZER for i in range(9)]
            self.historic_data[boardState] = queueValues

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

        agent_data = {}

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
            #agent_data[history[0]] = self.final_q_values

            if history[0] in agent_data:
                temp = self.get_largest_q_table(agent_data[history[0]], self.final_q_values)
                agent_data[history[0]] = temp
            else:
                agent_data[history[0]] = self.final_q_values



        #Compare dictionary to find the largest q table values for the given state.
        self.historic_data = self.dictionary_compare(agent_data, self.historic_data)


    def get_largest_q_table(self, array1, array2):
        a1 = sum(array1)
        a2 = sum(array2)

        if a2 > a1:
            return array2
        else:
            return array1

    def dictionary_compare(self, agent_data1, agent_data2):

        if len(agent_data1.keys()) > len(agent_data2.keys()):
            temp_dict = agent_data1
        else:
            temp_dict = agent_data2

        if temp_dict is None:
            return agent_data1
        else:
            for key in agent_data1:
                if key in temp_dict:
                    largest_q_table = self.get_largest_q_table(temp_dict[key], agent_data1[key])
                    temp_dict[key] = largest_q_table
                else:
                    temp_dict[key] = agent_data1[key]
            return temp_dict


    def save_to_file(self, queue_dict):
        if not os.path.exists('.\Data'):
            os.makedirs('.\Data')
        with open(filepath, "w") as file:
            for key in queue_dict:
                file.write(str(key) + ":" + str(queue_dict[key])[1:-1] + "\n")

    def load_to_dict(self):
        dict_values = {}

        if not os.path.exists(filepath):
            return dict_values
        else:
            file = open(filepath, "r")
            for line in file:
                line_split = line.split(":")
                values_split = line_split[1].split(",")
                array = []
                for i in values_split:
                    array.append(float(i))
                dict_values[line_split[0]] = array
            file.close()
            return dict_values
