def inches_to_feet(inches):
	if inches >= 12:
		return inches/12
	else:
		return 0

#or

def inches_to_feet(inches):
	return inches/12 if inches >= 12 else 0

#or

def inches_to_feet(inches):
	return inches //12