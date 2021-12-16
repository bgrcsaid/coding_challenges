def fifty_thirty_twenty(ati):
	return {
		'Needs'  : 0.5 * ati,
		'Wants'  : 0.3 * ati,
		'Savings': 0.2 * ati,
	}

#or

def fifty_thirty_twenty(ati):
    a = [(ati * 1/2), (ati * 3/10), (ati * 1/5)]
    b = ["Needs", "Wants", "Savings"]
    return dict(zip(b, a))