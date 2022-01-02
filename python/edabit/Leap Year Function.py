def leap_year(year):
	if year%4!=0:
		return False
	elif year%100!=0:
		return True
	elif year%400!=0:
		return False
	else:
		return True

#or

def leapYear(year):
    return year%400==0 or year%100!=0 and year%4==0

#or

from calendar import isleap as leapYear
