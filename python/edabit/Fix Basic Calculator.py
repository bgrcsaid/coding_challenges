def basic_calculator(a, o, b):
	result = 0

	if(o == "+"):
			return a + b
	elif(o == "-"):
			return a - b
	elif(o == "/" and b == 0):
			return None
	elif(o == "/"):
			return a / b
	elif(o == "*"):
			return a * b
	elif(o == "-" or "+" or "*" or "/"):
			return None
	return result

#or

ef basic_calculator(a, o, b):
    if (o=="/" and b!=0) or o in "+-*":
        return eval(str(a) + o + str(b))