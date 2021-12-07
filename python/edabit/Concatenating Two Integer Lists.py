def concat(lst1, lst2):
	return lst1+lst2

#or

def concat(lst1, lst2):
	lst1.extend(lst2)
	return lst1

#or

concat=lambda a,b:a+b