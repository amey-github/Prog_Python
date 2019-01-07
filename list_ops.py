#Commonly used functions
ex = [1,4,2,3]
ex.sort()
print ex

ex.append(5)
print ex

ex.pop(4)
print ex

ex.extend([5,6])
print ex

ex.reverse()
print ex

ex.remove(6)
print ex

#Comparison
list1 = [21,22,23]
list2 = [21,22,23]

# op == checks for same corresponding elements,"is" checks for same object
print (list1==list2)
print (list1 is list2)

list3 = list4 = [1,2,3]
print (list3 is list4)

sen = 'hey %s there %s'

#only tuples print vals accordingly
blah = ('yes','no')
print sen%blah

#lists cannot be used
#blah = ['yes','no']
#print sen%blah
#showws ERROR

pizza = 'dominos'
print ('s' in pizza)
print ('a' in pizza)
