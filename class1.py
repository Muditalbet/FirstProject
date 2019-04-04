class Calculator():
	def add(self,a,b):
		return a+b
	def subtract(self,a,b):
		return a-b
c=Calculator().add(5,2)
d=Calculator().subtract(5,2)
print("The add is",c,"and the subtract is",d)
