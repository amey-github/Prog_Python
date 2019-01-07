from operator import itemgetter

team = [
	{'fname':'Rohit', 	'lname':'Sharma'},
	{'fname':'Shikhar', 'lname':'999'},
	{'fname':'Virat', 	'lname':'Kohli'},
	{'fname':'MS', 		'lname':'Dhoni'},
	{'fname':'Shikhar', 'lname':'000'},
	{'fname':'Hardik', 	'lname':'Pandya'},
	{'fname':'Shardul', 'lname':'Thakur'}
]

fname_sort = sorted (team, key = itemgetter('fname'))			# Sorts only by 'fname'
print(fname_sort, '\n')

dict_sort = sorted (team, key = itemgetter('fname', 'lname'))	# Sorts 1st by 'fname', then by 'lname' within fname sort, i.e. sorts like a dictionary
print(dict_sort, '\n')