string=set(str(input("enter the string")))
count=0
vowels=set('aeiou')
for i in string:
	if i in vowels:
		count+=1
print('the vowels are',count)