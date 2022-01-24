def return_negative(n):
	if n<= 0:
		return n
	else:
		return - n

#or

def return_negative(n):
	return n if n<=0 else -n

#or

def return_negative(n):
	return - abs(n)
