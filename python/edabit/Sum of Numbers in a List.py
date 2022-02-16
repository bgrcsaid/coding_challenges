import math

def list_sum(lst):
    return sum(i**2 for i in lst if i%2==0) + round(sum(math.sqrt(i) for i in lst if i%2!=0),2)

#or

import math

def list_sum(lst):
	return round(sum(i**2 if i%2== 0 else math.sqrt(i) for i in lst), 2)

#or

def list_sum(lst):
    return round(sum(i ** 0.5 if i % 2 else i ** 2 for i in lst), 2)
