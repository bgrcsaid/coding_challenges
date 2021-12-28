def word(s):
	word = {
	'zero': 0,
	'one': 1,
	'two': 2,
	'three': 3,
	'four': 4,
	'five': 5,
	'six': 6,
	'seven': 7,
	'eight': 8,
	'nine': 9
	}
	return word[s]

#or

def word(s):
	x=["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
	return x.index(s)

#or

def word(s):
	return 'zero one two three four five six seven eight nine'.split(' ').index(s)
