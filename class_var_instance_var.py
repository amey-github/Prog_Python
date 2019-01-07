class ClassName:

	class_var = 1		# Every pbject of ClassName will have the var class_var

	def __init__(self, instance_var):
		self.instance_var = instance_var		# Every object created may/may not have th same val for instance_var

obj1 = ClassName(5)
obj2 = ClassName(10)

print('obj1:' obj1.class_var, obj1.instance_var)
print('obj2:' obj2.class_var, obj2.instance_var)