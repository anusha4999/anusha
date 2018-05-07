s1=(input('enter string'))
s2=(input('enter string'))
# a=set(s1)
# b=set(s2)
# c=list(a^b)
a=list(set(s1)^set(s2))
for i in a:
	print(i)
