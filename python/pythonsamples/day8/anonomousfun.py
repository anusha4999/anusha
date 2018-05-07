square=(lambda a:a**2)
square(2)
add_two_num=(lambda a,b:a+b)
add_two_num(10,20)
lm=[1,2,3]
l=list(map(lambda i:i+10,lm))
print(l)
l2=list(filter(lambda x:x%2==0,lm))
print(l2)
from functools import reduce
reduce(lambda x,y:x+y,lm)