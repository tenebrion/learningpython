#!/usr/bin/env python3
'''
Created on Mar 7, 2016
@author: Michael Koegel / mkoegel@gmail.com

Hangman

Sample XML Response: http://www.dictionaryapi.com/products/api-collegiate-dictionary.htm
Another option: http://www-personal.umich.edu/~jlawler/wordlist

My original intention was to use dictionary's API to pull random words for my hangman
game. However, from digging in, that may not be a feasible option since I have to pass
the API a full URL with a 'word' in it. Instead, I'll use option two which is a wordlist

This is all to learn to work with URL's, API's, translating XML documents, and of
course the game itself.
'''
import random
import urllib.request
from xml.dom.minidom import parse

print("Welcome to Hangman. You get 8 attempts to figure out the word!")


def make_random():
    word_site = urllib.request.urlopen(
        "http://www-personal.umich.edu/~jlawler/wordlist"
        )
    txt = word_site.read()
    words = txt.splitlines()
    random_word = str(random.choice(words))
    random_word =  ((random_word).replace("b'", "").replace("'", ""))
    return random_word

#setting a few initial variables
random_word = make_random()
game_board = ["#" for letter in random_word]
guessed_letters = []
play_again = True

#this is checking to ensure the letter hasn't been guessed already
def guessed(user_guess, letters):
    for chars in letters:
        if user_guess == chars:
            print("You've already guessed that letter. Please try again!")
            return

    # New letter, add it to the list and fill in the gameboard.
    guessed_letters.append(user_guess)
    #passing user_guess to another method
    fill_in_letter(user_guess)

#this method is replacing the ### symbols with the correctly guessed letter
#and putting the letter in the proper spot
def fill_in_letter(user_guess):
    #since the game_board is a list, have to swap
    #characters in a similar fashion
    for i in range(len(random_word)):
        if user_guess == random_word[i]:
            game_board[i] = user_guess
            print("We found a letter: '%s'" % (user_guess))
        
    #if all chars are revealed before the 8 turns are up, the user wins
    #I am having trouble wrapping my head around this last bit.
    if game_board == random_word:
        play_game(game_board)

#simple process of printing the game
def print_game(game_board):
    print(" ".join(game_board))

#this method checks to see if the user guesses the correct word.
def play_game(user_word):
    if user_word == random_word:
        print('You guessed the correct word. You WIN!')
        word_meaning(random_word)
        return True

    return False

#this section will call the dictionaryapi to define the word
#I only need to fix the formatting upon print. I may look at using
#regex to remove < > items
def word_meaning(random_word):
    #url call
    xml = urllib.request.urlopen(
                                 "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/" \
                                  + random_word + "?key=2fb6218d-a259-4bb1-af32-db6fe195cdc5")
    #I'll need a try, except here. I've found some words
    #that don't exist in their current state. For example,
    #jejunus has a potential match of jejunum...
    try:
        xml_file = parse(xml)
        ref_list = xml_file.getElementsByTagName("dt")
        #just stripping out the initial <dt>: tag
        print((ref_list[0].toxml()).replace("<dt>:", "").replace("</dt>", ""))
    except IndexError:
        print("Item not found in dictionary. It may be listed under another name.")

#this is the meat of the game. Right now it does basics of allowing 6 turns and a 'play again'
#option. However, the play again doesn't reset the turn number.
while play_again:
    for turn in range(8):
        print("Turn ", turn + 1)
        
        #if this is the first turn, print a simple message
        if (turn + 1) == 1:
            user_guess = (input("Please pick a letter: ")).lower()
        
        #any guess beyond the first guess prompts to see if the user wants to guess the word
        if (turn + 1) > 1:
            attempt_guess = (input("Would you like to guess the word? (y/n): ")).lower()
            
            if attempt_guess == "y":
                guess_word = (input("What is your guess? : ")).lower()
                if play_game(guess_word) == True:
                    #trying to allow additional games
                    play_more = (input("Wanna play another round (y / n)? ")).lower()
                    
                    #this ends the game totally
                    if play_more == "n":
                        play_again = False
                        quit()
                    #I don't know how to reset the turn counter yet.
                    #I may end up changing from a for loop to a while loop and
                    #add a counter - then reset the counter here.
                    elif play_more == "y":
                        make_random()
                    else:
                        quit()
            else:
                user_guess = (input("Please pick a letter: ")).lower()
    
        guessed(user_guess, guessed_letters)
        print("Currently guessed letters: %s" % (guessed_letters))
        print_game(game_board)
    
    #if the user hits the 8th turn and doesn't guess the word, game over
    if turn == 7:
        print("Game Over! The correct word is '%s'" % (random_word))
        word_meaning(random_word)
        
        #find out if the user wants to play more
        play_more = (input("Wanna play again (y / n)? ")).lower()
        
        #this section will determine next steps. Either end the game,
        #start over, or quit (in the event of something other than
        #y or n selections
        if play_more == "n":
            play_again = False
            quit()
        elif play_more == "y":
            make_random()
        else:
            quit()