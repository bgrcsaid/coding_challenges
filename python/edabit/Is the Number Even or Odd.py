def isEvenOrOdd(num):
	return "even" if num%2==0 else "odd"

#or

def isEvenOrOdd(num):
	return ["even", "odd"][num % 2]