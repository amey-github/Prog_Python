'''
Program to extract news_title - news_link from TOI pages
'''

import requests 					# To request info from web page
from bs4 import BeautifulSoup		# Go to the website and sort through data


def news_spider(max_pages):		# Limit max pgs scanned to make test run, debugging easy	
	page = 2
	
	while page <= max_pages:
		
		url = 'https://blogs.timesofindia.indiatimes.com/page/' + str(page) + '/'
		
		source_code = requests.get(url)
		plain_text = source_code.text
		soup = BeautifulSoup(plain_text, 'lxml')
			# BeautifulSoup class needs its data to be in a special format to crawl/sort through the links,etc
			# So we create a BeautifulSoup object to crawl through the source code		

		print('*************************PAGE NO.', page,'*************************', '\n')
		i = 1

		for link in soup.findAll('a', {'rel':'bookmark'}):
			# Goes through the source code and finds all of a specific item depending on info given
			# 'a' link tag, 'rel' element, 'Blog_Home_Pos#' search data
			# All search data related to result stored in link

			href = link.get('href')		# Filter href links from all data in var link
			title = link.string			# Filter title from all data in var link

			print(i, '.', title, ':', href, '\n')
			news_date_author(href)
			news_detail(href)
			
			i += 1

			if(i==2):	# Small sample to test run
				break
		
		page += 1


def news_date_author(news_url):			# Extract date, time and author of editing article

	source_code = requests.get(news_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, 'lxml')

	for link in soup.findAll('span',{'class':'date'}):
		datetime = link.text.strip()	# Ignores any wanted tags within the findAll() result
		print(datetime)

	for link in soup.findAll('a',{'class':'author'}):
		author = link.text.strip()
		print(author,'\n')


def news_detail(news_url):				# Extract details of article

	source_code = requests.get(news_url)
	plain_text = source_code.text
	soup = BeautifulSoup(plain_text, 'lxml')
 
	for link in soup.findAll('p'):

		detail = link.text.strip()
		print(detail, '\n')

news_spider(2)