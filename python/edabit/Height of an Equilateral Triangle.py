import math

def height(side):
	return str(round(math.sqrt(3)/2*side*10, 1)) + ' mm'

#or

def height(side):
	return '{:.1f} mm'.format(8.66 * side)
