l1=[[1,2],[3,4]]
l2=[[5,6],[7,8]]
l3=[[0,0],[0,0]]
for i in range(len(l1)):
	for j in range(len(l1[0])):
		l3[i][j]=l1[i][j]+l2[i][j]
for r in l3:
	print(r)

