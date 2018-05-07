def fun():
	try:
		c=5/0
		print(c)
	except ZeroDivisionError:
		print("there is a 0 in denomenator")
fun()
