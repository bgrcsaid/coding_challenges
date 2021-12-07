def find_smallest_num(lst):
	return min(lst)

#or

def find_smallest_num(lst):
    lst.sort()
    return lst[0]

#or

def findSmallestNum(lst):
	smallest=lst[0]
	for x in lst:
		if x < smallest:
			smallest = x
	return smallest