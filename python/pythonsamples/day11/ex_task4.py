class Error(Exception):
	'''this is the base exception class'''
class UnderAgeError(Error):
	'''this is error'''
class OverAgeError(Error):
	'''overage error'''
class NotYetBornError(Error):
	'''no born error'''
age=26
while True:
	try:
		x=int(input("enter age of a person"))
		if(x<=0):
			raise  NotYetBornError
		elif(x>age):
			raise OverAgeError
		elif(x<age):
			raise UnderAgeError
		else:
			print("correct guess")
	except OverAgeError:
		print("the person age is lessthan u are expected")
	except UnderAgeError:
		print("the person age is greaterthan u are expected")
	except NotYetBornError:
		print("the person  is not borned")
	finally:
		print("u have entered some age")
