"""
Shujee Iqbal
BCSF14M541
System Programming
Task 2: Searches given words in the top 5 articles in the latest news section of propakistani.pk
"""

from bs4 import BeautifulSoup
import requests
import datetime
import os
import sys

dict = {}

def getSource(urlstr):
	return requests.get(urlstr)
	
def parseMainPage(URL):
	r = getSource(URL)
	soup = BeautifulSoup(r.content, 'html.parser')
	rs = soup.find_all('div', {'class': 'single-story'})
	
	list = []
	
	for n in range(0,5):
		list.append(rs[n].find('a')['href'])
	
	return list
	
def parseArticles(URL):
	r = getSource(URL)
	soup = BeautifulSoup(r.content, 'html.parser')
	rs = soup.find_all('p')
	
	return rs
	
def find_word(word, rs, URL):
	for r in rs:
		if (word in r.text):
			val = dict.get(word, None)
			
			if (val == None):
				dict[word] = []
			dict[word].append(URL)
			break

def main():
	URL = "https://propakistani.pk"
	
	links = parseMainPage(URL)
	
	userinput = input("Enter words sperated by spaces: ") 
	
	print()
	
	words = userinput.split(' ')
	
	for link in links:
		rs = parseArticles(link)
		
		for word in words:
			find_word(word, rs, link)
			
	for word in words:
		print("Word \'{0}\' appears in :".format(word))
				
		val = dict.get(word, None)
		
		if (val == None):
			print("This word doesn't appear in top 5 links.")
			continue
		
		for links in dict[word]:
			print(links)
			
		print("...................")
	

if __name__ == "__main__":
    main()