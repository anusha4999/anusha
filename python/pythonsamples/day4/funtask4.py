def cal():
	'''calculator program using functions
	****menu****
	1.arithmetic operations
	2.relational operations
	3.logical operations
	4.bitwise operations
	5.boolean operations
	6.special operations
	7.assignment operations'''
	print(cal.__doc__)
	n=int(input('enter ur choice'))
	if(n==1):
		def cal1():
			'''
			1.addition
			2.substraction'''
			while(True):
				print(cal1.__doc__)
				x=int(input('enter ur choice:'))
				if(x>2):
					cal()
				else:
					a=int(input("enter a value:"))
					b=int(input('enter b value:'))
					if x==1:
						print("addition is:",a+b)
					if x==2:
						print("substraction is:",a-b)

		cal1()
		cal()
	elif(n==2):
		def cal2():
			'''
			1.lessthan
			2.greaterthan
			'''
			while(True):
				print(cal2.__doc__)
				x=int(input('enter ur choice:'))
				if(x>2):
					cal()
				else:
					a=int(input("enter a value:"))
					b=int(input('enter b value:'))
					if(x==1):
						print(a<b)
					if x==2:
						print(a>b)
		cal2()
		cal()
	elif(n==3):
		def cal3():
			'''
			1.logical and
			2.logical or
			'''
			while(True):
				print(cal3.__doc__)
				x=int(input("enter ur choice:"))
				if(x>2):
					cal()
				else:
					a=int(input("enter a value:"))
					b=int(input('enter b value:'))
					if(x==1):
						print('logical and',a and b)
					if(x==2):
						print('logical or',a or b)
		cal3()
		cal()
	elif(n==4):
		def cal4():
			'''
			1.bitwise and
			2.bitwise or
			'''
			while(True):
				print(cal4.__doc__)
				x=int(input("enter ur choice:"))
				if(x>2):
					cal()
				else:
					a=int(input("enter a value:"))
					b=int(input('enter b value:'))
					if x==1:
						print('bitwise and:',a&b)
					if x==2:
						print('bitwise or:',a|b)
		cal4()
		cal()
	elif(n==5):
		def cal5():
			'''
			1.boolean a
			2.boolean b
			'''
			while(True):
				print(cal5.__doc__)
				x=int(input('enter ur choice:'))
				if(x>2):
					cal()
				else:
					a=int(input("enter a value:"))
					b=int(input('enter b value:'))
					if x==1:
						print(bool(a))
					if x==2:
						print(bool(b))
		cal5()
		cal()
	else:
		#print("wrong selection")
		print(exit)
	
cal()