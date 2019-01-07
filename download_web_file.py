from urllib import request
import random

def get_file(file_url):

	response = request.urlopen(file_url)	# Stores connection to the web page in variable response
	print (response, '\n')					# To see what var response looks like

	csv = response.read()					# Reads all the data from file_url
	csv_str = str(csv)
	csv_lines = csv_str.split('\\n')			# Breaks up a string whenever it comes across '\n'

	dest_url = r'file_web' + str(random.randrange(1,1000)) + '.csv'
	file_exe = open(dest_url, 'w')

	for line in csv_lines:		
		file_exe.write(line + '\n')

	file_exe.close()

get_file(' http://insight.dev.schoolwires.com/HelpAssets/C2Assets/C2Files/C2ImportCalEventSample.csv')