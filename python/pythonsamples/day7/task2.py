import sys
import random
a=int(sys.argv[1])
for x in range(2):
	p=random.randrange(0,9)
	print(p,end='')
for y in range(a):
	q=chr(random.randrange(97,123))
	print(q,end='')
print(x)
