def calculate_exponent(num, exp):
	return num** exp

#or

def calculate_exponent(*args):
	return args[0]** args[1]

#or

from functools import reduce
import operator

def calculate_exponent(*args):
	return reduce(operator.pow, args)
