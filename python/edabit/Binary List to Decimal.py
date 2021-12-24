def binary_to_decimal(lst):
	return int("".join([str(i) for i in lst]), 2)

#or

def binary_to_decimal(lst):
	return int(''.join(map(str,lst)),2)
