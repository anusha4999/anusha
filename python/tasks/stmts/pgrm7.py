f1=0
f2=1
for i in range(1,51):
	if i<=1:
		f3=i
	else:
		
		f3=f1+f2
		f1=f2
		f2=f3
		print(f3)