def even_odd_string(txt):
	return txt[::2] + ' ' + txt[1::2]

#or

def even_odd_string(txt):
	return '{} {}'.format(txt[::2], txt[1::2])