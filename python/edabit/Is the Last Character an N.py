def is_last_character_n(word):
	return word[-1]== 'n'

#or

def is_last_character_n(word):
	return word.endswith('n')

#or

def is_last_character_n(word):
	return word[-1].lower() == 'n'
