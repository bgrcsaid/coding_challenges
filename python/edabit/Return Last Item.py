def last_ind(lst):
	return lst[-1] if lst!=[] and lst!="" else None

#or

def last_ind(lst):
	return lst[-1] if lst else None

#or

def last_ind(lst):
	return None if len(lst) == 0 else lst[-1}
