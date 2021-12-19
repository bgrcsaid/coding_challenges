def clean_up_list(lst):
  lst1 = [int(i) for i in lst if int(i)%2==0]
  lst2 = [int(i) for i in lst if int(i)%2!=0]
  return [lst1, lst2]

#or

def clean_up_list(lst):
    return [[int(i)for i in lst if int(i)%2==0],[int(i)for i in lst if int(i)%2!=0]]

#or

def clean_up_list(lst):
    return [[int(i) for i in lst if int(i)%2==m] for m in [0,1]]