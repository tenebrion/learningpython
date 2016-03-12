"""
The goal is to censor any type of word and not individual letters
"""
def censor(text, word): #passing two variables
	text = text.split() #splitting the string into single words
	
	#iterating through the items in the string from start to finish
	for items in range(len(text)):
		if text[items] == word: #if each item is the same as the word, proceed
			text[items] = (len(word) * "*") #this is where we replace the 'word' with the "*". It also has to be the same length as the 'word'
	return " ".join(text) #combining the words and * symbols with spaces.