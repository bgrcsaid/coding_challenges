def find_none(lst):
	if None in lst:
		return lst.index(None)
	else:
		return -1

#or

def find_None(lst):
	return lst.index(None) if None in lst else -1