def remove_numbers(string):
    return "".join(i for i in string if i.isalpha())

#or

def remove_numbers(string):
    return "".join(i for i in string if not i.isdigit())