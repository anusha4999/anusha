# a=[1,2,3,4]
# print(a.reverse())
# # a.reverse()
# # print(a)
# print(a.sort(reverse=True))
a=[i*i for i in range(1,10)]
print(a)
a=[]
b=[]
d={}
n=int(input("how many elements u want to add in dict"))
for i in range(1,n):
	a=(int)(input("enter key"))
	b=a*a
	for i in a:
		for j in b:
			d[i]=j
print(d)