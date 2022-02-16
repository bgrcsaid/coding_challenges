def programmers(one, two, three):
	return max(one,two,three) - min(one,two, three)

#or

def programmers(*args):
	return max(args)- min(args)

#or

def programmers(one, two, three):
	lst=[one,two,three]
	return(max(lst)- min(lst))
