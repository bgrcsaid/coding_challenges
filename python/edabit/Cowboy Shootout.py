def roger_shots(lst):
	return (lst.count('Bang!') + lst.count('BangBang!'))/2

#or

def roger_shots(lst):
	return sum(i in ('Bang!', 'BangBang!') for i in lst)/2
