def list_to_string(lst):
	return ''.join([str(i) for i in lst])

#or

def list_to_string(lst):
		return ''.join(map(str, lst))
