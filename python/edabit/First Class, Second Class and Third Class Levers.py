def determine_lever(l):
	if l[1]=="f":
		return "first class lever"
	elif l[1]=="l":
		return "second class lever"
	elif l[1]=="e":
		return "third class lever"
        
#or

def determine_lever(lev):
	return ('third', 'first', 'second')[lev.index('f')] + ' class lever'