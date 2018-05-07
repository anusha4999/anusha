class samp:
	def __init__(self,name,dept):
		
			self.name=name
			self.dept=dept
			def student(self):
				print(self.name)
				print(self.dept)
obj=samp(anusha,mca)
setattr(obj,'name','anusha')
obj.student()
getattr(obj,'name','anusha')
obj.student()