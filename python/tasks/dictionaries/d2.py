dic1={1:10, 2:20}
dic2={3:30, 4:40}
for i in (dic1, dic2):
	 dic2.update(i)
print(dic2)