print 'EXAMPLE 1 -'
class parent1:
    var1 = 'parent 1'

class parent2:
    var1 = 'parent 2'

class child(parent1, parent2): #parent2 called, then parent1 called
    var3 = 'child'

obj = child()
print obj.var1
#print obj.var2
print obj.var3

"''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"

print '\nEXAMPLE 2 -'
class parent1:
    var1 = 'parent 1'

class parent2:
    var2 = 'parent 2'

class child(parent1, parent2): #parent2 called, then parent1 called
    var3 = 'child'

obj = child()
print obj.var1
print obj.var2
print obj.var3
