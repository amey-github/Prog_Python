list_var = ['juice', '11/07/18', 20]
name, date, price = list_var
print(name, date, price)

def firstLastGrades(*grades):		# Tuple which can accept dynamic num of elements
	
	print(grades)
	first, *middle, last = grades
	avg = sum(middle)/len(middle)
	print(avg)

firstLastGrades(1, 5, 10, 15, 2)