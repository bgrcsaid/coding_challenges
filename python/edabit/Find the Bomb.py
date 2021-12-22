def bomb(txt):
	return "Duck!!!" if "bomb" in txt.lower() else "There is no bomb, relax."

#or

def bomb(s): 
	return ['There is no bomb, relax.', 'Duck!!!']['bomb' in s.lower()]