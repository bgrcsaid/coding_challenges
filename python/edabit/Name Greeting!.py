def hello_name(name):
	return "Hello " + name +'!'

#or

def hello_name(name):
	return ("Hello %s!") % name

#or

def hello_name(name):
	return "Hello {}!".format(name)
