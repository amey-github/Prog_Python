'''
Instead of passing vals when calling function
We can pass a list of t vals
'''

def multiply(a, b, c):
	ans = a*b*c;
	print "multiply",ans

num_args = [2,3,4]
multiply(*num_args)