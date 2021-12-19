def amazing_edabit(s):
	return s.replace('amazing', 'not amazing') if 'edabit' not in s else s

#or

def amazing_edabit(s):
    return s if 'edabit' in s else s.replace('amazing','not amazing')