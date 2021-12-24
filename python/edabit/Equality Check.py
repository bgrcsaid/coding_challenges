def check_equality(a, b):
	return type(a) is type(b) and bool(a) == bool(b)

#or

def check_equality(a, b):
	return a is b
