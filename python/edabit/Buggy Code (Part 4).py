def greeting(name):
	if name == "Mubashir":
		return "Hello, my Love!"
	else:
		return "Hello, " + name + "!"

#or

def greeting(name):
	return 'Hello, {}!'.format('my Love' if name == 'Mubashir' else name)