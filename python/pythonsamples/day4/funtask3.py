l=[1,2,3,4,5]
print(l)
n=int(input('enter the number:'))
def lis(l):
	for i in l:
		if n==i:
			print(l.index(n))
lis(l)