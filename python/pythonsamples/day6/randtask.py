import sys
import random
a=int(sys.argv[1])
for x in range(a):
	print(random.randrange(0,9),end='')
print()
for y in range(a):
	print(chr(random.randrange(97,123)),end='')