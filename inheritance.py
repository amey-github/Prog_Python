class Parent:

	def parent_fn(self):
		print('parent_fn')

class Child(Parent):				# INHERITS FROM A SINGLE PARENT

	def child_fn(self):
		print('child_fn')

'''	def parent_fn1(self):			# OVERRIDES THE PARENT FUNCTION if we define the parent_function in Child
		print('Overrides the parent_function1 inherited from Parent')'''

print('Parent object')
obj = Parent()
obj.parent_fn()