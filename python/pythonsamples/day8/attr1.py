class samp:
	def __init__(self,a,b):
			self.a=a
			self.b=b
	def student(self):
			print(self.a)
			print(self.b)
s=samp(10,20)
setattr(s,'a','12')
s.student()
print(getattr(s,'a'))
print(hasattr(s,'a'))
s.student()