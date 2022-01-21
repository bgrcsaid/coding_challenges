def equilibrium(x):
    return "positive" if x > 0 else "negative" if x < 0 else True

#or

def equilibrium(x):
	return x == 0 or ('negative','positive')[x> 0]
