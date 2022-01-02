def modify_last(txt, n):
	if n==0:
		return txt[0:-1]
	else:
		return txt + txt[-1]*(n-1)

#or

def modify_last(txt, n):
    return txt[:-1] + txt[-1] * n
