class ClassName:

	def __init__(self, n):		# default name for constructor in python: __init__(self, *args)
        
		self.num = n
		print('Automatically prints without being called')
		print(self.num)
        
	def function(self):
        
		print('\nPrints only when called')
		self.num += 1
		print(self.num)

obj = ClassName(5)		# arguments passed do not include 'self'
obj.function()