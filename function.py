def math_ops(x,y):
    print 'Add : ', x+y
    print 'Sub : ', abs(x-y)
    print 'Mul : ', x*y
    print 'Div : ', float(x)/y
    print 'Exp : ', x**y


x = int(raw_input('Enter x : '))
y = int(raw_input('Enter y : '))

print'\n'

math_ops(x,y)