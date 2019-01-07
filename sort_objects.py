from operator import attrgetter

class ClassName:

	def __init__(self, x, y):
		
		self.var1 = x
		self.var2 = y


	def __repr__(self):			# Define representation of the objects of class ClassName
		return self.var1 + ':' + str(self.var2)


obj_list = [
	ClassName('a', 99),
	ClassName('z', 0),
	ClassName('c', 15)
]

for obj in obj_list:
	print(obj)


print('\n')
sort_obj_list = list(sorted(obj_list, key = attrgetter('var1')))

for obj in sort_obj_list:
	print(obj)


print('\n')
sort_obj_list = list(sorted(obj_list, key = attrgetter('var2')))

for obj in sort_obj_list:
	print(obj)