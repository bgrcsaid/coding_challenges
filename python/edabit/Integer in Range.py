def int_within_bounds(n, lower, upper):
	return n >= lower and n < upper and isinstance(n, int)

#or

def int_within_bounds(n, lower, upper):
	return n in range(lower, upper)