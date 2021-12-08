def calculate_fuel(n):
	if n<=10:
		return 100
	else:
		return 10*n

#or

def calculate_fuel(n):
	return max(n*10, 100)