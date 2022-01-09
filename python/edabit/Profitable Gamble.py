def profitable_gamble(prob, prize, pay):
	if prob * prize > pay:
		return True
	else:
		return False

#or

def profitable_gamble(prob, prize, pay):
	return prob * prize > pay
