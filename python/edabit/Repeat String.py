def repeat_string(txt, n):
	return txt*n if type(txt)==str else "Not A String !!"

#or

def repeat_string(txt, n):
	return txt*n if isinstance(txt, str) else 'Not A String !!'