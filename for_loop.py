one = ['a','b','c','d']

for i in range(len(one)):
    print i, one[i]

'''
To print nums alongside strings
Use "," to seperate the 2 values/vars (in place of the generally used +)
print(str_var, num_var)
'''

print '\n'

for letter in one:
    print letter

print '\n'

# range(<start_pt>, <end_pt>, <increment_by>)
for i in range(0,4, 2):
    print i, one[i]

print '\n'

#for dictionary
ages = {'mom':40, 'dad':50 , 'sis':15}

for val in ages:
    print val, ages[val]

#does not work for "while" loop
