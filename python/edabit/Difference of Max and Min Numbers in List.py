def difference_max_min(lst):
	a = min(lst)
	b = max(lst)
	return b-a

#or

def difference_max_min(lst):
	return max(lst) - min(lst)

#or

def difference_max_min(lst):
	lst.sort()
	return lst[-1] - lst[0]

#or

def difference_max_min(lst):
	return abs(min(lst) - max(lst))