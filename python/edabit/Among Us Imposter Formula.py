def imposter_formula(i, p):
	return "{:.0%}".format(round(i/p, 2))

#or

def imposter_formula(i, p):
	return str(round(100*(i/p))) + "%"