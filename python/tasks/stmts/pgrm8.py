n=int(input('integer'))
for i in range(2):
	print('*'*n)
	for j in range(int(n/2)-1):
		print('*',end='')
		for j in range(n-2):
			print(' ',end='')
		print('*',end='')
		print()