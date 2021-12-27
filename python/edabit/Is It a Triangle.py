def is_triangle(a, b, c):
	lst=sorted([a,b,c])
	return lst[0]+lst[1]>lst[2]

#or

def is_triangle(a, b, c):
	a, b, c = sorted((a, b, c))
	return a + b > c

#or

def is_triangle(a, b, c):
	return a + b > c and b + c > a and a + c >
