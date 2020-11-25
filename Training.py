from TabularTrainer import *
from GameBoard import *
from TicTacToe import *

action_to_coordinate = {0: (0, 0), 1: (0, 1), 2: (0, 2),
                        3: (1, 0), 4: (1, 1), 5: (1, 2),
                        6: (2, 0), 7: (2, 1), 8: (2, 2)}
LOSING_PENALTY = 0
WINNING_REWARD = 1
TIE_REWARD = 0.5

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
        gameResult = 0;

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
        gameResult = game.determine_winner()
        #TODO: gameResult not calculating correctly

        #TODO: make a function similar to final_result in example code
        #agent1.result(gameResult)
        #agent2.result(gameResult)
        return gameResult

    def evaluateMove(self, agent, game):
        move = agent.move(game.game_board)
        if move == -1:
            return True
        coord = action_to_coordinate[move]
        game.game_board.setSpaceTaken(coord)
        finished = game.is_game_over()
        return finished

#TODO: I was thinking we could use this function to compare the two agents or data over time
'''
    def evalv(board, agent1, agent2):
        #play the game for a number rounds
        #use the move history to calcu
        #at the end, the best players qtable weights are the ones we save
        pass
'''
