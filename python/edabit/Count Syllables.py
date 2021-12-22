def number_syllables(word):
	return word.count("-")+1

#or

def number_syllables(word):
	return len(word.split('-'))