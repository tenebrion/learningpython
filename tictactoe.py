"""
Fun game of tic tac toe
"""
game_board = {"1": " ", "2": " ", "3": " ",
              "4": " ", "5": " ", "6": " ",
              "7": " ", "8": " ", "9": " "}


def print_board(board):
    """
    printing out the board
    :param board: passing game_board['X']
    :return:
    """
    print("{}|{}|{}".format(board["1"], board["2"], board["3"]))
    print("-+-+-")
    print("{}|{}|{}".format(board["4"], board["5"], board["6"]))
    print("-+-+-")
    print("{}|{}|{}".format(board["7"], board["8"], board["9"]))


player_turn = "X"
print("\nThis is the classic game of tic tac toe.\n"
      "Moves are mapped out as top row = 1, 2, or 3.\n"
      "Middle row = 4, 5, or 6 and bottom row = 7, 8, or 9\n")

for i in range(9):
    print_board(game_board)
    print("It is {}'s turn. Where would you like to move?".format(player_turn))
    try:
        move = int(input())
        game_board[move] = player_turn
    except ValueError:
        move = input("Invalid entry. Please try again: ")
        game_board[move] = player_turn

    if player_turn == "X":
        player_turn = "O"
    else:
        player_turn = "X"

print_board(game_board)
