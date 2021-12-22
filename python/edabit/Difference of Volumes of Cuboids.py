from functools import reduce
import operator

def find_difference(a, b):
	return abs(reduce(operator.mul, b) - reduce(operator.mul, a))

#or

def find_difference(a, b):
	l1,w1,h1 = a
	l2,w2,h2 = b
	return abs((l1*w1*h1)-(l2*h2*w2))