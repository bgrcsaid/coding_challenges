def who_wins_tonight(coins, space, price, size):
	if coins//price < space//size:
		return "Will"
	elif coins//price > space//size:
		return "Bill"
	else:
		return "Tie"

#or

def who_wins_tonight(coins, space, price, size):
	return 'Tie' if coins//price==space//size else ['Will', 'Bill'][coins//price>space//size]