def circuit_power(voltage, current):
	return voltage*current
  
#or

from functools import reduce
import operator

def circuit_power(*args):
	return reduce(operator.mul, args, 1)
