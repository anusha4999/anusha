l1=[]
l2=[]
l3=[]
l4=[]
res=[[0,0],[0,0]]
x=[]
y=[]
n=int(input('enter no of rows:'))
m=int(input('no of columns:'))
print('enter values or first matrix:')
print('enter column values:')
for i in range(0,m):
	z=int(input('enter values:'))
	l1.append(z)
x.append(l1)
print('enter row values:')
for j in range(0,n):
	p=int(input('enter values:'))
	l2.append(p)
x.append(l2)
print(x)
print('enter values or second matrix:')
print('enter column values:')
for i in range(0,m):
	z=int(input('enter values:'))
	l3.append(z)
y.append(l3)
print('enter row values:')
for j in range(0,n):
	p=int(input('enter values:'))
	l4.append(p)
y.append(l4)
print(y)
for i in range(len(x)):
	for j in range(len(y[0])):
		for c in range(len(y)):
			res[i][j]+=x[i][c]*y[c][j]
for k in res:
	print(k)
