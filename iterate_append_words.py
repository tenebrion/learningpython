def iterate_words(word):
	char_list = []
	
	for char in word:
		char_list += char
	
	return char_list

print(iterate_words("gleaning"))
