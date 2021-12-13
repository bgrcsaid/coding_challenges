def add_binary(a, b):
	return bin(a+b)[2:]

#or

def add_binary(a, b):
	return "{0:b}".format(a+b)