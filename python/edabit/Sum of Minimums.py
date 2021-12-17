def sum_minimums(lst):
	if len(lst)==3:
		return min(lst[0])+min(lst[1])+min(lst[2])
	elif len(lst)==4:
		return min(lst[0])+min(lst[1])+min(lst[2])+min(lst[3])

#or

def sum_minimums(lst):
	return sum(min(i) for i in lst)

#or

def sum_minimums(lst):
	return sum(map(min, lst))