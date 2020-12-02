from TabularTrainer import *
from RandomPlayer import *
from NNQTrainer import *
from TicTacToe import *
import matplotlib.pyplot as plt

action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                        3: (1, 0), 4: (1, 1), 5: (1, 2),
                        6: (2, 0), 7: (2, 1), 8: (2, 2)}

#NOTE: tried to keep anything updating the board in this tile so we could use the TicTacToe functions
class Training:

    def begin_training(self, number_of_battles = 100):
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
            agent1_wins.append(agent1Win)
            agent2_wins.append(agent2Win)
            draws.append(draw)
            counter = counter + 1
            count.append(counter)

        self.visualize_training_results(count, agent1_wins, agent2_wins, draws)
        print("training ended")

    def battleRounds(self, number_of_games = 1000):
        agent1 = TabularTrainer('O', 'Agent 1')
        agent2 = TabularTrainer('X', 'Agent 2')
        #agent2 = RandomPlayer('X', 'Agent 2')

        agent1WinCount = 0
        agent2WinCount = 0
        drawCount = 0

        for i in range(0, number_of_games):
            print("game " + str(i))
            winner = self.playGame(agent1, agent2, number_of_games)
            if winner == 1:
                agent1.save_to_file(agent1.historic_data)
                agent1WinCount += 1
            elif winner == 2:
                agent2.save_to_file(agent2.historic_data)
                agent2WinCount += 1
            else:
                agent1.save_to_file(agent1.historic_data)
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

        finished = game.is_game_over()

        return finished

    def get_game_results(self, game, agent1, agent2) -> int:
        winner = 0

        if game.game_won:
            if game.winning_player == game.player_one:
                agent1.result("won")
                agent2.result("loss")
                winner = 1
            else:
                agent1.result("loss")
                agent2.result("won")
                winner = 2
        elif game.tie_game:
            agent1.result("tie")
            agent2.result("tie")

        #Tabular Trainer against itself
        higher_q_values = self.see_who_has_higher_qvalues(agent1.final_q_values, agent2.final_q_values)

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
        agent1_wins_perc = (agent1_wins / (agent2_wins + agent1_wins + draws)) * 100
        agent2_wins_perc = (agent2_wins / (agent2_wins + agent1_wins + draws)) * 100
        draws_perc = (draws / (agent2_wins + agent1_wins + draws)) * 100

        plt.plot(gameNum, agent1_wins_perc)
        plt.plot(gameNum, agent2_wins_perc)
        plt.plot(gameNum, draws_perc)
        plt.title('Battle Round Metrics')
        plt.legend(['Agent 1 Wins', 'Agent 2 Wins', 'Draws'])
        plt.xlabel('Battle Round Number')
        plt.ylabel('Percentage of Agent Wins or Draws')
        plt.show()

        plt.bar(gameNum, agent1_wins_perc)
        plt.bar(gameNum, agent2_wins_perc)
        plt.bar(gameNum, draws_perc)
        plt.title('Battle Round Metrics')
        plt.legend(['Agent 1 Wins', 'Agent 2 Wins', 'Draws'])
        plt.xlabel('Battle Round Number')
        plt.ylabel('Percentage of Agent Wins or Draws')
        plt.show
