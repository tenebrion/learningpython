guessed_letters = ["a", "e", "i"]


def guessed(user_guess, letters):
	"""
	checking to see if the user already guessed those letters

	:param user_guess: str
	:param letters: str
	"""
	for chars in letters:
		if user_guess == chars:
			return "You've already guessed that letter. Please try again!"
		else:
			guessed_letters.append(user_guess)
			return guessed_letters

print(guessed("t", guessed_letters))
