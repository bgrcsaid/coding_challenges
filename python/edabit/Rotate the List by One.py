def rotate_by_one(lst):
    return lst[-1:]+lst[:-1]

#or

def rotate_by_one(lst):
    return [lst[-1]]+lst[0:-1]

#or

def rotate_by_one(lst):
    lst.insert(0, lst.pop())
    return lst
