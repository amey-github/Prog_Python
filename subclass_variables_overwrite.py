class parent:
    var1 = 'parent 1'
    var2 = 'parent 2'

class child(parent):
    var1 = 'child 1'

par = parent()
chi = child()

print 'PARENT:'
print par.var1,'\n',par.var2

print '\nCHILD:'
print chi.var1,'\n',chi.var2
