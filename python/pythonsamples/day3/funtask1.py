l=[i for i in range(1,20) if i%2!=0]
#print(l)
def avg(l):
	#for i in l:
		a=sum(l)
		b=a//len(l)
		print('mean is :',b)
avg(l)
def median(l):
	#for i in l:
		n=len(l)
		if(len(l)%2==0):
			n1=(l[n//2]+l[(n//2)-1])
			print('median is %d,' %(n1//2))
		else:
			print(l[n//2])
median(l)

	
		
		