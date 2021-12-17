def add_parity_bit(b):
  return b+"1" if b.count("1", 0, len(b))%2!=0 else b+"0"

#or

def add_parity_bit(b):
	return b + ['0', '1'][b.count('1') % 2]