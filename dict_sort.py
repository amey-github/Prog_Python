import operator

dict_name = {
	'b': 2,
	'a': 3,
	'c': 1,
}

# SORTING METHOD 1 --- Using loop

for letter, num in sorted(dict_name.items(), key = operator.itemgetter(1)):
	print(letter, num)


'''
SORTIG METHOD 2 --- Using zip

zip(dict_name.values(), dict_name.keys()) splits the dictionary into 2 lists
1 of values, 2 of keys

'''

print(sorted(zip(dict_name.values(), dict_name.keys())))		# Sorts by 'values' in the dict_name

print(sorted(zip(dict_name.keys(), dict_name.values())))		# Sorts by 'keys' in the dict_name

print(min(zip(dict_name.values(), dict_name.keys())), max(zip(dict_name.values(), dict_name.keys())))