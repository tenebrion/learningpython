from random import randint

# enabling a debug mode that will print the random number to the screen
debug_enabled = True

# computer generated number ranging between 1 and 100
random_num = randint(1, 20)

if debug_enabled:
    # need to print the random number
    print("Debug Mode Enabled: The random number is {}".format(random_num))


def number_range(user_num, rand_num):
    """
    This method will check to see how close the user's guess is to the
    actual number. Based on that, it will spew out different messages
    to help guide the person closer to the number.

    :param user_num: num
    :param rand_num: num
    """
    if 1 <= abs(user_num - rand_num) <= 2:
        return "You are HOT!"
    elif 3 <= abs(user_num - rand_num) <= 5:
        return "You are getting WARMER!"
    elif 6 <= abs(user_num - rand_num) <= 8:
        return "You are COLD!"
    else:
        return "You are NOT close!"

for turn in range(10):
    print("Turn", turn + 1)

    while True:
        try:
            if (turn + 1) == 1:
                # asking the user to input a number
                user_guess = int(input("Guess a number between 1 and 20: "))
                break
            elif (turn + 1) >= 2:
                user_guess = int(input("Guess a different number between 1 and 20: "))
                break
            else:
                break
        except ValueError:
            user_guess = int(input("Your input was not an integer. Please try again: "))
            break
    else:
        break
    
    # if the guess is outside of the range, post a message
    if user_guess < 1 or user_guess > 20:
        print("Your guess is outside the range of our game.")
    else:
        # if the user guesses the correct answer on the first attempt, print a message
        if (user_guess == random_num) and (turn + 1 == 1):
            print("You WIN! You guessed the correct number on your first try! AWESOME!")
            break
        
        # if the user guesses the correct number on attempt 2 through 10, print a message
        if (user_guess == random_num) and (turn + 1 >= 2):
            print("You WIN! It took you {} attempts to guess the right number".format(turn + 1))
            break
    
    # passing the values to the method to compare
    print(number_range(user_guess, random_num))

if turn == 9:
    print("Out of turns. Game Over!")