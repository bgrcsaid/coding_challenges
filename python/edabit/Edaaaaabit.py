def how_many_times(num):
	return "Ed{}bit".format(num*'a')

#or

def how_many_times(num):
	txt = "Edabit"
	return txt.replace("a", "a"*num)

#or

def how_many_times(num):
	a = 'a'
	return'{}{}{}'.format('Ed',a*num,'bit')