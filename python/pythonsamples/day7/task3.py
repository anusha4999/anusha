d={}
a=input('enter username')
f=open('d:\python\pythonsamples\day7\pqr1.py','a')
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
d={a:l}
f.writelines('\n')
#f.writelines(l)
f.writelines(d)
f.close()
print(d)
for i in d.keys():
	if a==i:
		print('existed user')
		break
	else:
		d={a:l}
		#print(l)
print(d)
