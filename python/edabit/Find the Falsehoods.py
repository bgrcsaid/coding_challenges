def find_the_falsehoods(lst):
		return list(i for i in lst if bool(i) == False)

#or

def find_the_falsehoods(lst):
	return [i for i in lst if not i]
