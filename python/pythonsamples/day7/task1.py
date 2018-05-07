f=open('d:\python\pythonsamples\day7\pqr.py','a')
import random
l=''
for x in range(2):
	for y in range(4):
		q=chr(random.randrange(97,123))
		l=l+q
	for y in range(4):
		p=str(random.randrange(0,9))
		l=l+p
print(l)
f.writelines('\n')
f.writelines(l)

