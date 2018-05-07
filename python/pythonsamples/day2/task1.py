n=int(input("enter how many times u want"))
a=[]
b=[]
d={}
for i in range(1,n):
	a=input('enter key')
	b=input('enter value')
	#a.append(b)
	#d=a.append(b)
	#c=dict(zip(a,b))
	for i in a:
		for j in b:
			d[i]=j

print(d)