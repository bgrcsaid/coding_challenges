def yeah_nope(b):
	return "yeah" if b==True else "nope"

#or

def yeah_nope(b):
	return "yeah" if b else "nope"

#or

def yeah_nope(b):
	return ['nope', 'yeah'][b]
