def makes10(a, b):
	if a+b==10 or a==10 or b==10:
		return True
	else:
		return False

#or

def makes10(a, b):
  return 10 in [a,b,a+b]

#or

makes10=lambda a,b : 10 in [a,b,a+b]
