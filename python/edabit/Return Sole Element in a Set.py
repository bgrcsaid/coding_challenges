def element_from_set(s):
	return s.pop()

#or

def element_from_set(s):
	return list(s)[0]

#or

def element_from_set(s):
	for i in s:
		return i
