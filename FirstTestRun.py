from TicTacToe import *
from Player import *


def first_tests():
    ticky = TicTacToe(Player('X', 'Player 1'), Player('O', 'Player 2'))
    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    ticky.play_round((0, 0))

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    ticky.play_round((0, 1))

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (0, -1)
    if not ticky.isValidMove(move):
        print("Move out of bounds!")
    else:
        ticky.play_round(move)

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (-1, -1)
    if not ticky.isValidMove(move):
        print("Move out of bounds!")
    else:
        ticky.play_round(move)

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (-1, 0)
    if not ticky.isValidMove(move):
        print("Move out of bounds!")
    else:
        ticky.play_round(move)

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (0, 4)
    if not ticky.isValidMove(move):
        print("Move out of bounds!")
    else:
        ticky.play_round(move)

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (0, 0)
    if not ticky.isValidMove(move):
        print("Move invalid!")
    else:
        ticky.play_round(move)

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (0, 1)
    if not ticky.isValidMove(move):
        print("Move invalid!")
    else:
        ticky.play_round(move)

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (0, 2)
    if not ticky.isValidMove(move):
        print("Move invalid!")
    else:
        ticky.play_round(move)

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (0, 2)
    if not ticky.isValidMove(move):
        print("Move invalid!")
    else:
        ticky.play_round(move)

    print(ticky.get_current_player_tag() + "'s Turn: " + ticky.get_current_player().getPlayerSymbol())
    ticky.get_board().display_board()
    move = (1, 0)
    if not ticky.isValidMove(move):
        print("Move invalid!")
    else:
        ticky.play_round(move)
        print("Move success: ")
        ticky.get_board().display_board()
