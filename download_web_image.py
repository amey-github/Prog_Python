import random
import urllib.request	#module that allows us to get data from websites

def get_image(source_url):
	name = 'img' + str(random.randrange(1,1000))
	file_name = name + '.jpeg'

	urllib.request.urlretrieve(source_url, file_name)	# image is stored in the same directory as the program file

'''
Python can't concatenate numbers and strings
Unless specified explicitly using type coversion
'''

get_image('https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiivrDz7dbdAhXYWisKHbFvA1AQjRx6BAgBEAU&url=https%3A%2F%2Fvectorcharacters.net%2Fgeek-vector-characters%2Fboy-vector-character-with-bag-and-notepad&psig=AOvVaw2RITLhTMVCvQooRXuKaUx6&ust=1537989020552355')

'''
This prog can be used to input url from user in real time
And download to downloads folder
'''
