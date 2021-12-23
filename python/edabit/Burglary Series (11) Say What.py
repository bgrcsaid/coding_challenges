def say_what(obj):
	return " ".join(obj.values()) + ' ' + obj[2]

#or

def say_what(obj):
	return ' '.join(obj[i] for i in obj) + ' ' + obj[2]

#or

def say_what(obj):
	return ' '.join([i for i in obj.values()]) +  ' '  + obj.get(2)