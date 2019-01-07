class parent:
    var1 = 1
    var2 = 'i am var2'

class child1(parent):
    pass #simply means <no content>

class child2(parent):
    pass

parObj = parent()
obj1 = child1()
obj2 = child2()

print obj1.var1
print obj2.var2
