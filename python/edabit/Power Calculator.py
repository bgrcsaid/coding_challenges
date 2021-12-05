def circuit_power(voltage, current):
	return voltage*current
  
#or

def circuit_power(*args):
	return args[0]*args[1]

#or

from functools import reduce
import operator

def circuit_power(*args):
	return reduce(operator.mul, args)
