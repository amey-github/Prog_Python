'''
the num of arguments is not known beforehand
args - flexible arguments parameter
'''

def add_num(*args):
	total = 0

	for a in args:
		total += a

	print "add",total

add_num(2,4)
add_num(2,4,16)

