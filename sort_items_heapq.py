import heapq

list_name = [5, 10, 15, 20, 25]
no_of_val = 3

print(heapq.nlargest(no_of_val, list_name))		# Returns 3 largest vals from list_name


list_dict = [						# Behaves like a 2D matrix
	{'name':'a', 'price':1},
	{'name':'b', 'price':2},		# list_dict[1]['price'] gives 2, list_dict[1]['name'] gives 'b'
	{'name':'c', 'price':3},
	{'name':'d', 'price':4},
	{'name':'e', 'price':5}
]

print(heapq.nsmallest(2, list_dict, key = lambda list_dict : list_dict['price']))