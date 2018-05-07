num=int(input('enter a number'))
sum=0
n=num
while n>0:
	rem=n%10
	sum=sum+rem*rem*rem
	#n//=10
	n=n//10

if num==sum:
	print('ams')
else:
	print('not a ams')
