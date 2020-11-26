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
        move = agent.move(game.game_board, game)

        if move == -1:
            return True

        coord = action_to_coordinate[move]

        game.play_round(coord)

        game.game_board.setSpaceTaken(coord)

        finished = game.is_game_over()

        return finished

    def get_game_results(self, game, agent1, agent2):
        print("game results")
        if game.game_won == True:
            print("game won")
            if game.winning_player == game.player_one:
                print("player 1 won")
                agent1.result(game.player_one)
            else:
                print("player 2 won")
                agent2.result(game.player_two)
        elif game.tie_game == True:
            print("game tie")
            #pass
            # logic for getting the game result for the tied game

#TODO: I was thinking we could use this function to compare the two agents or data over time
'''
    def evalv(board, agent1, agent2):
        #play the game for a number rounds
        #use the move history to calcu
        #at the end, the best players qtable weights are the ones we save
        pass
'''
