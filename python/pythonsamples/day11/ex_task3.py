try:
	c=5/0
	print(c)
except ZeroDivisionError:
	print('error')
finally:
	print('there is an error')