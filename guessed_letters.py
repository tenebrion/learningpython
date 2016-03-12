guessed_letters = ["a", "e", "i"]

def guessed(user_guess, letters):
	for chars in letters:
		if user_guess == chars:
			return "You've already guessed that letter. Please try again!"
		else:
			guessed_letters.append(user_guess)
			return guessed_letters

print(guessed("t", guessed_letters))
