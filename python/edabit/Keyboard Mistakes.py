def keyboard_mistakes(txt):
	table=txt.maketrans('4501','ASOI')
	return txt.translate(table)

#or

def keyboard_mistakes(txt):
	txt = txt.replace("4", "A")
	txt = txt.replace("5", "S")
	txt = txt.replace("0", "O")
	txt = txt.replace("1", "I")
	return txt