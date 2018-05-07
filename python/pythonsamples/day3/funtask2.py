l=[2,4,7,1,0,4,8,3,5]
def avg(l):
		a=sum(l)
		b=a//len(l)
		print('mean is :',b)
avg(l)
def median(l):
		n=len(l)
		if(len(l)%2==0):
			n1=(l[n//2]+l[(n//2)-1])
			print('median is %d,' %(n1//2))
		else:
			print(l[n//2])
median(l)
