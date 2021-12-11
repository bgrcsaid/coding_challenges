def check(lst, el):
	return el in lst

#or

def check(lst, el):
	for i in range(len(lst)):
		if lst[i] == el:
			return True
	return False