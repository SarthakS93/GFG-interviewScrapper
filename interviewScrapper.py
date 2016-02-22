import pdfkit
from bs4 import BeautifulSoup
import requests

mainURL = 'http://www.geeksforgeeks.org/tag/snapdeal/'
visited = {}
path = '/home/sarthak/mvFiles/'

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
			if 'snapdeal-interview' in temp:
				if not temp.split('/')[-1] == '#respond':
					myLinks.append(temp)

	if 'snapdeal-interview' in url:
		save_PDF(url)

	for i in myLinks:
		if not i in visited:
			magic(i)


def save_PDF(url):
	print(url)
	name = url.split('/')[-2]
	pdfkit.from_url(url, path + name)

magic(mainURL)