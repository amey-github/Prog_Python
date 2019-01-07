tina = [18, 'HHS', 'pune']
bob = [3, 'kidzee', 'delhi']

sibling = {'tina':tina, 'bob':bob}

print sibling
print sibling['tina']

print '\n'

for key, val in sibling.items():
	print key, val

print '\n'

#diff b/w copy() method and assignment op =
#used for dictionaries

family = sibling.copy()		# same result as family = sibling
print family				# family.clear() is to clear a set
print sibling

print '\n'

sibling = {'tina':tina, 'bob':bob}
sibling.has_key('tina')
sibling.has_key('john')

print sibling.keys()


#INVALID statement
#sibling['bob'[1]]