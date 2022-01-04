def operate(num1, num2, operator):
	return eval(str(num1)+operator+str(num2))

#or

import operator
def operate(n1,n2,o):
	ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '%' : operator.mod,
    '^' : operator.xor,
	}

	return ops[o](n1,n2)
