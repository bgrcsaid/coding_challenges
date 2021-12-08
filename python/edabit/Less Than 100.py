def less_than_100(a, b):
	if a+b<100:
		return True
	else:
		return False

#or

def less_than_100(a, b):
	return a + b < 100

#or

less_than_100 = lambda a,b: a+b < 100