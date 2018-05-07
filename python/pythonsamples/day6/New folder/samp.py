fread=open('d:/python/pythonsamples/day6/sampfile.txt','a')
count=0
for i in fread:
	if i=='\n':
		count+=1
if count==4:
	fread.write('hello good evening')
fread.close()
