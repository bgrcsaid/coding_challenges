def reverse_capitalize(txt):
	return txt.upper()[:: -1]

#or

def reverse_capitalize(txt):
	return txt[:: -1].upper()
