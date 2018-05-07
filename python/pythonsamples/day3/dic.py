l1=[]
l2=[]
d={}
for i in range(1,6):
	key=int(input("enter key"))
	value=str(input("enter value"))
	print(l1.append(key))
	print(l2.append(value))
d=dict(zip(l1,l2))
print(d)