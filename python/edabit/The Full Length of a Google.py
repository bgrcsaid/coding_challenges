def googlify(n):
	return 'G' + n* 'o'+ 'gle' if n>1 else 'invalid'

#or

def googlify(n):
	return 'G{}gle'.format('o' *n) if n> 1 else 'invalid'
