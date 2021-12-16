def should_serve_drinks(age, on_break):
	return age >= 18 and on_break==False

#or

def should_serve_drinks(age, on_break):
  return age > 17 and not on_break