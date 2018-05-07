import random
# print(dir(random))
a=random.randint(1,10)
print('random integer no:',a)
b=random.randrange(1,50,3)
print('random range:',b)
l=[1,2,3,4]
random.shuffle(l)
print(l)
c=random.choice(l)
print('choice of list:',c)
print(random.random())
