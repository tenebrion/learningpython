'''
Created on Feb 24, 2016

@author: michael.f.koegel
'''
"""
To do: add multiple battle ships and make sure they don't overlap
       add random sized battle ships and make sure they don't overlap or go off the board
       make the board larger
       make the game two player
       add rematches, game statistics
"""

#need to import the random integer section from the 'random' function
from random import randint

#defining the board and leaving it blank. This will get filled in.
board = []

#this is filling in the board with 'O''s to hide the ship
for x in range(5):
    board.append(["O"] * 5) #this actually adds the 'O''s

#Lets print the board without the [] or commas
def print_board(board):
    for row in board:
        print(" ".join(row)) # neat way to leave spaces without the [] or ""

print("Let's play Battleship!")
print_board(board) #just printing the board

#this function puts the ship in a random row
def random_row(board):
    return randint(0, len(board) - 1) #the -1 is important since tables start at 0 and not 1

#this function puts the ship on a random column
def random_col(board):
    return randint(0, len(board[0]) - 1) #The -1 is important since tables start at 0 and not 1

ship_row = random_row(board) #calling the row function to prep the ship for battle
ship_col = random_col(board) #calling the col function to prep the ship for battle
#print ship_row #this is used for debugging
#print ship_col

#the for loop is setting the user up with 4 guesses, which go 0-3
for turn in range(4):
    print("Turn", turn + 1) #should print Turn 1, Turn 2, etc.
    
    guess_row = int(input("Guess Row (1-5):")) #this is the row the user guesses
    guess_col = int(input("Guess Col (1-5):")) #this is the column the user guesses
    
    while (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
        print("Oops, that's not even in the ocean we're playing in...")
        break #found out I need to put a break here or else fear the wrath of an infinite loop!
        #guess_row = int(input("Please guess a new Row (1-5):")) #this is the row the user guesses
        #guess_col = int(input("Please guess a new Col (1-5):")) #this is the column the user guesses
    else:
        #checking to see if the user guesses the same stuff as the random ship
        if guess_row == ship_row and guess_col == ship_col:
            print("Congratulations! You sunk my battleship!") #woo the user won!
            break #stop the infinite loops!
        else:
            #checking to see if the user already guessed this attempt
            if (board[guess_row][guess_col] == "X"):
                print("You guessed that one already.")
            else: #if they didn't guess right and didn't guess the same thing, no hit
                print("You missed my battleship!")
                board[guess_row][guess_col] = "X" 

if turn == 3: #if the user is done with the 4th guess, they lose
    print("Out of turns. Game Over!")    
    print_board(board)