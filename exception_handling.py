while True:
	
	try:
		num = int(input("Type a number\n"))
		print(20/num)
		break

	except ValueError:
		print('Invalid Input!!')

	except ZeroDivisionError:
		print("Don't input zero")

	except:
		print('A general way to handle all types of errors')

	finally:
		print('This line is executed no matter what')