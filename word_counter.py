import requests			# To seek info from webpages and specified URls
import operator
from bs4 import BeautifulSoup

def getWordList(url):		# Creates a list of every word on the webpage
	
	word_list = []
	source_code = requests.get(url).text
	soup = BeautifulSoup(source_code, 'lxml')

	for link in soup.findAll('a', {'rel':'bookmark'}):
		content = link.string
		words = content.lower().split()		# lower() converts to lower case for consistency, split() splits content into individual words

		for each_word in words:
			word_list.append(each_word)

	#print(word_list, '\n\n')
	cleanUpList(word_list)


def cleanUpList(word_list):		# Removes unwanted characters (. , :) from each word element is word_list[]

	clean_word_list = []
	letters = "qwertyuiopasdfghjklzxcvbnm0123456789"

	for word in word_list:

		letters_list = []		# Needs to be reset every time to prevent fusing individual words
		clean_word = ''
			
		for i in range(len(word)):

			for j in range(len(letters)):			# Creating a letters_list[] for word filtering out unwanted characters
				if(word[i]==letters[j]):
					letters_list.append(word[i])

		if(len(letters_list) > 0): 
			clean_word = ''.join(letters_list)		# Fn to convert letters_list[] into string clean_word

		if (len(clean_word) > 0):			#  Eliminate case of any word like :) which gets replaced as "" creating issues in word counts
			clean_word_list.append(str(clean_word))

	createDictionary(clean_word_list)


def createDictionary(clean_word_list):

	word_count = {}						# Contains - 'word': count
	for word in clean_word_list:

		if word in word_count:			# If word already exists in word_count, +1 to its count
			word_count[word] += 1

		else:							# If word doesn't exist in the word_count, add the word and set count = 1
			word_count[word] = 1

	for word, count in sorted(word_count.items(), key = operator.itemgetter(1), reverse = True):
		print(word, '-', count)

	'''	
	sorted (what_to_sort, key = operator.itemgetter(1), reverse = True)
		
		key : parameter passed to specify basis for sort
		operator : predefined python fns for many mathematical, logical, relational, bitwise etc operations under the module “operator”
		itemgetter(val) : fn that returns the item based on word (val=0) or count (val=1)
		reverse = boolean : parameter specifying ascending (boolean=False) or descending (boolean=True)
	'''


getWordList('https://blogs.timesofindia.indiatimes.com/')

'''
word_count = {}						# Contains - 'word': count
	for word in clean_word_list:

		if word in word_count:			# If word already exists in word_count, +1 to its count
			word_count[word] += 1

		else:							# If word doesn't exist in the word_count, add the word and set count = 1
			word_count[word] = 1

	for word, count in sorted(word_count.items(), key = operator.itemgetter(1), reverse = True):
		print(word, '-', count)

	print(word_count)
'''