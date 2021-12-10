def sum_lst(lst):
	total = 0
	for i in range(0,len(lst)):
		total += lst[i]
	return total

#or

def sum_lst(lst):
  return sum(lst)