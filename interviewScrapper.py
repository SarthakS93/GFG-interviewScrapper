import pdfkit
from bs4 import BeautifulSoup
import requests
import os
import sys

mainURL = 'http://www.geeksforgeeks.org/tag/'
visited = {}
mainPath = os.path.dirname(os.path.abspath('interviewScrapper.py'))
target = sys.argv[1]
url = mainURL + target + '/'
os.makedirs(target)
path = mainPath + '/' + target + '/'
pattern = target + '-interview'

def magic(url):
	if url in visited:
		return
	visited[url] = True
	r = requests.get(url)
	soup = BeautifulSoup(r.text)
	myFind = soup.find_all('a')
	myLinks = []

	for l in myFind:
		if l.has_attr('href'):
			temp = l.get('href')
			if pattern in temp:
				if not temp.split('/')[-1] == '#respond':
					myLinks.append(temp)

	if pattern in url:
		save_PDF(url)

	for i in myLinks:
		if not i in visited:
			magic(i)


def save_PDF(url):
	print(url)
	name = url.split('/')[-2]
	pdfkit.from_url(url, path + name + '.pdf')

#magic(mainURL)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Please enter valid arguments")
    else:
        magic(url)