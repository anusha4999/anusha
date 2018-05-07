def avg(a,b,*args):
	sum=a+b
	for i in args[0]:
		sum=sum+i
	avg=sum//(len(args[0])+2)
	print(avg)
avg(10,20,[30,40,50])
