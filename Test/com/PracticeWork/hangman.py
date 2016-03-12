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

print("Welcome to Hangman. You get 6 attempts to figure out the word!")

#temporary word list. I'll eventually pull words from an API (or website)
word_list = ["hypocrite", "bellicose", "impertinent", "dispensation",
             "humility", "love", "denial", "uncomfortable", "asinine",
             "thug", "rhyme", "orgy", "creates", "massive", "erection"]

#setting a few intitial variables
random_word = random.choice(word_list)
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
    #trying to replace the specific # with the letter once guessed properly
    for i in range(len(random_word)):
        if user_guess == random_word[i]:
            game_board[i] = user_guess
            print("We found a letter: '%s'" % (user_guess))
        
        #if all chars are revealed before the 6 turns are up, the user wins

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
    #I need to teach myself how to format the url so it can reside on multiple lines and still work
    xml = urllib.request.urlopen("http://www.dictionaryapi.com/api/v1/references/collegiate/xml/" + random_word + "?key=2fb6218d-a259-4bb1-af32-db6fe195cdc5")
    xml_file = parse(xml)
    ref_list = xml_file.getElementsByTagName("dt")
    #just stripping out the initial <dt>: tag
    print((ref_list[0].toxml()).replace("<dt>:",""))

#this is the meat of the game. Right now it does basics of allowing 6 turns and a 'play again'
#option. However, the play again doesn't reset the turn number.
while play_again:
    for turn in range(6):
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
                    else:
                        quit()
            else:
                user_guess = (input("Please pick a letter: ")).lower()
    
        guessed(user_guess, guessed_letters)
        print("Currently guessed letters: %s" % (guessed_letters))
        print_game(game_board)
    
    #if the user hits the 6th turn and doesn't guess the word, game over
    if turn == 5:
        print("Game Over! The correct word is '%s'" % (random_word))
        word_meaning(random_word)