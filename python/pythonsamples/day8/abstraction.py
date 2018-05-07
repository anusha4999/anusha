class exponent:
	__a=4
	def power(self,b):
		self.__a**=b
		print(self.__a)
obj=exponent()
obj.power(2)
print(obj._exponent__a)