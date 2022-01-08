def next_element(lst):
	espace = lst[1]-lst[0]
	lst.append(lst[-1]+espace)
	return lst[-1]

def next_element(lst):
	return lst[-1]+(lst[1]-lst[0])
