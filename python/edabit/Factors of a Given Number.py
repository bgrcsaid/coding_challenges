def find_factors(n):
	return [i for i in range(1, n+1) if n%i==0]

#or

def find_factors(n):
	factors = []
	for i in range(1, n+1):
		if n%i==0:
			factors.append(i)
	return factors
