from TabularTrainer import *
from RandomPlayer import *
from TicTacToe import *
import matplotlib.pyplot as plt

action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                        3: (1, 0), 4: (1, 1), 5: (1, 2),
                        6: (2, 0), 7: (2, 1), 8: (2, 2)}

NUM_OF_BATTLES = 10
NUM_OF_GAMES = 50
#NOTE: tried to keep anything updating the board in this tile so we could use the TicTacToe functions
class Training:

    def begin_training(self, number_of_battles = NUM_OF_BATTLES):
        print("training started")
        # Have own while loop to play game
        agent1_wins = []
        agent2_wins = []
        draws = []
        count = []
        counter = 0

        for i in range(0, number_of_battles):
            print("battle " + str(i))
            agent1Win, agent2Win, draw = self.battleRounds()
            # Need to figure out the math depending on the number of games
            # we want it to show like in the example code (I might not have explained that clearly oops)
            agent1_wins.append((agent1Win / (agent1Win + agent2Win + draw)) * 100)
            agent2_wins.append((agent2Win / (agent1Win + agent2Win + draw)) * 100)
            draws.append((draw / (agent1Win + agent2Win + draw)) * 100)
            counter = counter + 1
            count.append(counter * NUM_OF_GAMES)

        self.visualize_training_results(count, agent1_wins, agent2_wins, draws)
        print("training ended")

    def battleRounds(self, number_of_games = NUM_OF_GAMES):
        agent1 = TabularTrainer('O', 'Agent 1')
        #agent2 = TabularTrainer('X', 'Agent 2')
        agent2 = RandomPlayer('X', 'Agent 2')

        agent1WinCount = 0
        agent2WinCount = 0
        drawCount = 0

        for i in range(0, number_of_games):
            print("game " + str(i))

            winner = self.playGame(agent1, agent2, number_of_games)

            if winner == 1:
                if isinstance(agent1, TabularTrainer):
                    agent1.save_to_file()
                    agent1.historic_data.clear()
                agent1WinCount += 1
            elif winner == 2:
                if isinstance(agent2, TabularTrainer):
                    agent2.save_to_file()
                    agent2.historic_data.clear()
                agent2WinCount += 1
            else:
                drawCount += 1


        return agent1WinCount, agent2WinCount, drawCount

    def playGame(self, agent1, agent2, number_of_games) -> int:
        game = TicTacToe(agent1, agent2)

        finished = False

        while not finished:
            finished = self.evaluateMove(agent1, game)
            if finished:
                break
            else:
                finished = self.evaluateMove(agent2, game)
                if finished:
                    break

        game.determine_winner()

        winner = self.get_game_results(game, agent1, agent2)

        return winner

    def evaluateMove(self, agent, game):
        move = agent.move(game.game_board)

        if move == -1:
            return True

        coord = action_to_coordinate[move]

        game.play_round(coord)

        game.game_board.setSpaceTaken(coord)

        finished = self.game_is_finished(game.get_board_grid())

        return finished

    def game_is_finished(self, board):
        game_over = False

        if np.all((board == 0)):
            game_over = True
        if (board[0, 0] > 0) and (board[0, 0] == board[0, 1] == board[0, 2]):
            game_over = True
        if (board[1, 0] > 0) and (board[1, 0] == board[1, 1] == board[1, 2]):
            game_over = True
        if (board[2, 0] > 0) and (board[2, 0] == board[2, 1] == board[2, 2]):
            game_over = True
        if (board[0, 0] > 0) and (board[0, 0] == board[1, 1] == board[2, 2]):
            game_over = True
        if (board[0, 2] > 0) and (board[0, 2] == board[1, 1] == board[2, 0]):
            game_over = True
        if (board[0, 0] > 0) and (board[0, 0] == board[1, 0] == board[2, 0]):
            game_over = True
        if (board[0, 1] > 0) and (board[0, 1] == board[1, 1] == board[2, 1]):
            game_over = True
        if (board[0, 2] > 0) and (board[0, 2] == board[1, 2] == board[2, 2]):
            game_over = True

        return game_over

    def get_game_results(self, game, agent1, agent2) -> int:
        winner = 0

        if game.game_won:
            if game.winning_player == game.player_one:
                if isinstance(agent1, TabularTrainer):
                    agent1.result("won")
                if isinstance(agent2, TabularTrainer):
                    agent2.result("loss")
                winner = 1
            else:
                if isinstance(agent1, TabularTrainer):
                    agent1.result("loss")
                if isinstance(agent2, TabularTrainer):
                    agent2.result("won")
                winner = 2
        elif game.tie_game:
            if isinstance(agent1, TabularTrainer):
                agent1.result("tie")
            if isinstance(agent2, TabularTrainer):
                agent2.result("tie")

        #Tabular Trainer against itself
        if isinstance(agent2, TabularTrainer) and isinstance(agent1, TabularTrainer):
            higher_q_values = self.see_who_has_higher_qvalues(agent1.final_q_values, agent2.final_q_values)

        #Tabular Trainer against RandomPlayer
        if isinstance(agent2, RandomPlayer):
            higher_q_values = agent1.final_q_values
        if isinstance(agent1, RandomPlayer):
            higher_q_values = agent2.final_q_values

        return winner

    def see_who_has_higher_qvalues(self, agent1_q_values, agent2_q_values):
        agent1 = 0.0
        agent2 = 0.0

        for i in range(0, len(agent1_q_values)):
            agent1 += agent1_q_values[i]
            agent2 += agent2_q_values[i]

        if agent1 > agent2:
            return agent1_q_values
        elif agent1 < agent2:
            return agent2_q_values

        # Default would be if the q values are equal
        return agent1_q_values

    #Plot the number of games each agent wins and ties
    def visualize_training_results(self, gameNum, agent1_wins, agent2_wins, draws):

        plt.plot(gameNum, agent1_wins)
        plt.plot(gameNum, agent2_wins)
        plt.plot(gameNum, draws)
        plt.title('Battle Round Metrics')
        plt.legend(['Agent 1 Wins', 'Agent 2 Wins', 'Draws'])
        plt.xlabel('Number of Games')
        plt.ylabel('Percentage of Agent Wins or Draws')
        plt.show()

