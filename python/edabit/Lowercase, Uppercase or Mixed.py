def get_case(txt):
	if txt.islower():
		return 'lower'
	if txt.isupper():
		return 'upper'
	else:
		return 'mixed'

#or

def get_case(txt):
	return 'upper' if txt.isupper() else 'lower' if txt.islower() else 'mixed'
