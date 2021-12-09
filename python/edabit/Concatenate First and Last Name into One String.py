def concat_name(first_name, last_name):
	return last_name + ', ' + first_name

#or

def concat_name(first_name, last_name):
	return ', '.join([last_name, first_name])

#or

def concat_name(first_name, last_name):
	return "{0}, {1}".format(last_name, first_name)