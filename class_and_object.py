class ClassName:		# Convention to start ClassName with caps; Class is a bluprint/prototype for an object
	var1 = 1

	def function1(self):		# 'self' means use something from own class		
		print('Function1 : Val of var1 =', self.var1)		# 'self' needs to be used to access the variable defined in the scope of class
		self.var1 += 1

	def function2(self):		
		print('Function2 : Val of var1 =', self.var1)

# Using only function1() gives error as you need to use objects to access anything inside a class

obj1 = ClassName()		# Objects contain a copy of  all information within a class
obj2 = ClassName()

obj1.function1()
obj1.function2()

print('\nEach object is independent of other objects')
obj2.function2()