def sum_five(lst):
	sum=0
	for i in lst:
		if i>5:
			sum = sum+i
	return sum

#or

def sum_five(lst):
	return sum(i for i in lst if i>5)
