def trimmed_averages(lst):
	lst.remove(max(lst))
	lst.remove(min(lst))
	return round(sum(lst)/len(lst))

#or

def trimmed_averages(lst):
	return round(sum(sorted(lst)[1:-1]) / (len(lst) - 2))
