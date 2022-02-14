def is_first_superior(lst1, lst2):
  for i in range(len(lst1)):
    if lst1[i] >lst2[i]:
      return True
  return False

#or

def is_first_superior(lst1,lst2):
	return lst1 > lst2
