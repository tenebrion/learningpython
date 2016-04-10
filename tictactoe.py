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


def check_winner():
    """
    Just a placeholder (something). This method will check the game_board
    and look for various wins (3 in a row).
    :param something: not sure what I'm going to use here
    :return:
    """
    # mapping out possible win combinations
    possible_wins = (game_board["1"] == game_board["2"] == game_board["3"],
                     game_board["4"] == game_board["5"] == game_board["6"],
                     game_board["7"] == game_board["8"] == game_board["9"],
                     game_board["1"] == game_board["4"] == game_board["7"],
                     game_board["2"] == game_board["5"] == game_board["8"],
                     game_board["3"] == game_board["6"] == game_board["9"],
                     game_board["1"] == game_board["5"] == game_board["9"],
                     game_board["3"] == game_board["5"] == game_board["7"])

    # testing the output
    for row in possible_wins:
        print(row)


player_turn = "X"
print("This is the classic game of tic tac toe.\n"
      "Moves are mapped out as:"
      "\nTop row = 1, 2, or 3"
      "\nMiddle row = 4, 5, or 6"
      "\nBottom row = 7, 8, or 9\n")

for i in range(9):
    print_board(game_board)
    while True:
        print("It is {}'s turn. Where would you like to move?".format(player_turn))
        try:
            # I'm hacking together a cheap way to verify inputs. I've thought about
            # making the board input text based (e.g. TL, TM, TR, ML, MM, MR, LL, LM, LR)
            move = int(input())
            if 1 <= move <= 9:
                game_board[str(move)] = player_turn
                break
            elif 0 <= move <= 10:
                print("Your selection is outside the range, please try again.")
                continue
            else:
                print("Please enter an integer between 1 - 9")
                continue
        except ValueError:
            print("Please enter integers only.")
            continue

    if player_turn == "X":
        player_turn = "O"
    else:
        player_turn = "X"

print_board(game_board)
check_winner()
