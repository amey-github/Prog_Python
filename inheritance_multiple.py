class Parent1:

	def parent_fn1(self):
		print('parent_fn1')

class Parent2:

	def parent_fn2(self):
		print('parent_fn2')

class Child1(Parent1):				# INHERITS FROM A SINGLE PARENT

	def child_fn1(self):
		print('child_fn1')

class Child2(Parent1, Parent2):		# INHERITS FROM A MULTIPLE PARENT

	def child_fn2(self):
		print('child_fn2')


print('Parent1 object')
obj1 = Parent1()
obj1.parent_fn1()


print('\nParent2 object')
obj2 = Parent2()
obj2.parent_fn2()


print('\nChild1 object')
obj3 = Child1()
obj3.parent_fn1()
obj3.child_fn1()


print('\nChild2 object')
obj4 = Child2()
obj4.parent_fn2()
obj4.child_fn2()


class Useless():		# To leave a class blank, use keyword 'pass'
	pass