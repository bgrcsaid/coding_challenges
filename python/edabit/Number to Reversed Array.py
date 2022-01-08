def reverse_list(num):
	return [int(i) for i in str(num)[::-1]]

#or

def reverse_list(num):
  return list(map(int,reversed(str(num))))
