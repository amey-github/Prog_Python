list1 = ['a', 'b', 'c']
list2 = ['1', '2', '3']

list3 = zip(list1, list2)	# zip() ties the corresponding elements of the lists entered, returs a zip() object

list3 = list(list3)			# converting zip() object to list type

for i,j in list3:
	print(i,j)

for i in range(len(list3)):
	print(list3[i])

print(list3)