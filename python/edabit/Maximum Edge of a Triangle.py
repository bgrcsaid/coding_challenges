def next_edge(side1, side2):
	return (side1+side2)- 1

#or

def next_edge(*args):
	return sum(args) -1
