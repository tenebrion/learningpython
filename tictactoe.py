"""
Fun game of tic tac toe
"""
game_board = {"top-L": " ", "top-M": " ", "top-R": " ",
              "mid-L": " ", "mid-M": " ", "mid-R": " ",
              "low-L": " ", "low-M": " ", "low-R": " "}


def print_board(board):
    """
    printing out the board
    :param board: passing game_board['X']
    :return:
    """
    print("{}|{}|{}".format(board["top-L"], board["top-M"], board["top-R"]))
    print("-+-+-")
    print("{}|{}|{}".format(board["mid-L"], board["mid-M"], board["mid-R"]))
    print("-+-+-")
    print("{}|{}|{}".format(board["low-L"], board["low-M"], board["low-R"]))


player_turn = "X"

for i in range(9):
    print_board(game_board)
    print("It is {}'s turn. Where would you like to move?".format(player_turn))
    move = input()
    game_board[move] = player_turn

    if player_turn == "X":
        player_turn = "O"
    else:
        player_turn = "X"

print_board(game_board)
