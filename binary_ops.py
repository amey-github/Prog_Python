# Binary AND, OR, XOR.......

a = 50		# 110010
b = 25		# 011001

c = a & b	# 010000
print(c)

c = a | b	# 111011
print(c)

c = a ^ b	# 101011
print(c)


# Binary RIGHT SHIFT, LEFT SHIFT.........

x = 240		# 11110000

y = x >> 2	# 00111100, shift bits 2 places to the right, vacant left spots occuppied by 0
print(y)

y = x << 2	# 1111000000, shift bits 2 places to the left, vacant right spots occuppied by 0
print(y)