list_name = [1, 2, 3]

def fnName(list_arg):
	return list_arg * 2

new_list = list(map(fnName, list_name))		# Substitutes running through the list using for-loop
print(new_list)