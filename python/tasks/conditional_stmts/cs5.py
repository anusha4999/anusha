a=int(input('enter a value'))
b=int(input('enter b value'))
c=int(input('enter c value'))
if a>b and a>c:
	print('a is big',a)
elif b>a and b>c:
	print('b is big',b)
else:
	print('c is big',c)