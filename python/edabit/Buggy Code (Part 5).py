def print_list(n):
	result=[]
	i=1
	while i<=n:
		result+=[i]
		i += 1
	return result

#or

def print_list(n):
    return list(range(1, n+1))