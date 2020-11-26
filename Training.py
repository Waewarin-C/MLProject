from TabularTrainer import *
from GameBoard import *
from TicTacToe import *

action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                        3: (1, 0), 4: (1, 1), 5: (1, 2),
                        6: (2, 0), 7: (2, 1), 8: (2, 2)}

#NOTE: tried to keep anything updating the board in this tile so we could use the TicTacToe functions
class Training:

    def begin_training(self):
        # Have own while loop to play game
        self.battleRounds()
        print("training started")

    def battleRounds(self):
        agent1 = TabularTrainer('O', 'Agent 1')
        agent2 = TabularTrainer('X', 'Agent 2')
        drawCount = 0
        agent1Count = 0
        agent2Count = 0
        self.playGame(agent1, agent2)
        #TODO: I was think we can just do battle rounds vs the running 10000 time 10 games etc.
        #initiate the playGame for the players
        #update the counts for win, loss, or draw

    def playGame(self, agent1, agent2):
        game = TicTacToe(agent1, agent2)

        finished = False
        print("start loop")
        i = 0
        while not finished:
            finished = self.evaluateMove(agent1, game)
            if finished:
                break
            else:
                finished = self.evaluateMove(agent2, game)
                if finished:
                    break
            i = i + 1

        game.determine_winner()

        self.get_game_results(game, agent1, agent2)

    def evaluateMove(self, agent, game):
        move = agent.move(game.game_board)

        if move == -1:
            return True

        coord = action_to_coordinate[move]

        game.play_round(coord)

        game.game_board.setSpaceTaken(coord)

        finished = game.is_game_over()

        return finished

    def get_game_results(self, game, agent1, agent2):
        if game.game_won:
            if game.winning_player == game.player_one:
                agent1.result("won")
                agent2.result("loss")
            else:
                agent1.result("loss")
                agent2.result("won")
        elif game.tie_game:
            agent1.result("tie")
            agent2.result("tie")

        higher_q_values = self.see_who_has_higher_qvalues(agent1.final_q_values, agent2.final_q_values)

        # TODO: find a way to save the higher_q_values

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

#TODO: I was thinking we could use this function to compare the two agents or data over time
'''
    def evalv(board, agent1, agent2):
        #play the game for a number rounds
        #use the move history to calcu
        #at the end, the best players qtable weights are the ones we save
        pass
'''
