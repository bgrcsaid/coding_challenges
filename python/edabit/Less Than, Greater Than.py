def list_between(num1, num2, lst):
	return list(i for i in lst if i>num1 and i<num2)

#or

def list_between(num1, num2, lst):
    return [i for i in lst if num1 < i < num2]