def find_single_number(numbers):
	for i in set(numbers):
		if numbers.count(i) == 1:
			return i