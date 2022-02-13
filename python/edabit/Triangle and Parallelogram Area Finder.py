def area_shape(base, height, shape):
	if shape =="triangle":
		return 0.5*base*height
	else:
		return base* height

#or

def area_shape(b,h,f):
	return b*h * 0.5 if f=='triangle' else b*h

#or

def area_shape(base, height, shape):
	return base * height / [1, 2][shape == "triangle"]
