import operator

def age_difference(ages):
	difference = operator.sub(sorted(ages)[-1], sorted(ages)[-2])
	if difference == 0:
		return "No age difference between spouses."
	elif difference == 1:
		return str(operator.sub(sorted(ages)[-1], sorted(ages)[-2])) + " year"
	elif difference > 1:
		return str(operator.sub(sorted(ages)[-1], sorted(ages)[-2])) + " years"

#or

def age_difference(ages):
	a, b  = sorted(ages)[-2:]
	diff  = b - a
	return "No age difference between spouses." if diff == 0 else '{} year{}'.format(diff, ('s', '')[diff == 1])