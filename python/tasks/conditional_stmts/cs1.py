tmarks=int(input("enter total marks"))
omarks=int(input("enter obtained marks"))
per=(omarks/tmarks)*100
print(per)
if per>=85:
	print("a grade")
elif((per<85) or (per>60)):
	print("b grade")
else:
	print("c grade")

'''marks=int(input("enter marks"))
if marks<=600:
	print('grading is possible')
	if marks>=500:
		print('a grade')
	elif marks<500 and marks>350:
		print('b grade')
	else:
		print('c grade')
else:
	print('grading not possible')'''