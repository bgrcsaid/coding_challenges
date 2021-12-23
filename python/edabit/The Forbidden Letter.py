def forbidden_letter(char, lst):
	return not any(char in i for i in lst)

#or

def forbidden_letter(char, lst):
	return all(char not in i for i in lst)

#or

def forbidden_letter(char, lst):
	return char not in "".join(lst)