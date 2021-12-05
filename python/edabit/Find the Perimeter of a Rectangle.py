def find_perimeter(length, width):
	return length*2 + width*2

#or

def find_perimeter(length, width):
    return 2*(length+width)
    
#or

def find_perimeter(*args):
	return 2*(args[0]+args[1])
