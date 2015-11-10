from bs4 import BeautifulSoup
import urllib.request
import re

url = 'https://boardgamegeek.com/browse/boardgame'
page = urllib.request.urlopen(url)
soup = BeautifulSoup(page.read())
x = 0
text = open('saveHtml.txt', 'w')

gamename = soup.find_all('td', class_="collection_objectname")
for x in range(0, 50):
	html_tag = gamename[x].find_next("a")
	with open('saveHtml.txt', 'w'):
		text.write("https://boardgamegeek.com" + html_tag['href'] + '\n')
	

