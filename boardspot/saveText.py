from bs4 import BeautifulSoup
import urllib.request
import re
import codecs
import html.parser

filename = open('saveHtml.txt', 'r')
line = 0
for line in range(0, 50):
	url = filename.readline()	
#url = 'https://boardgamegeek.com/boardgame/12333/twilight-struggle'
	page = urllib.request.urlopen(url)
	soup = BeautifulSoup(page.read())
	url = url.strip("abcdefghijklmnopqrstuvwxyz.:/-")

	gamename = soup.find("meta", {"name":"title"})['content']
	gamename = gamename.replace(" ", "_")

	number = url.split('/')[0]	
	numofplayers = soup.find("div", {"id":"results_players_thing_" + number}).text
	numofplayers = numofplayers.strip('\t\r\n')
	numofplayers = numofplayers.encode('utf-8')
	players = str(numofplayers)[1:].replace('\\xc2\\xa0\\xe2\\x88\\x92\\xc2\\xa0', '-')

	ages = soup.find("div", {"id":"results_minage_thing_" + number}).text
	ages = ages.strip('\t\r\n')
	ages = ages.strip("and up")
	ages = ages.strip('\t\r\n')
	
	playtime = soup.find("div", {"id":"results_playtime_thing_" + number}).text
	playtime = playtime.strip('\t\r\n')
	playtime = playtime.encode('utf-8')
	time = str(playtime)[1:].replace('\\xc2\\xa0\\xe2\\x88\\x92\\xc2\\xa0', '-')
	
	genrename = ""
	genre = soup.find_all(href=re.compile("boardgamecategory"))[1:]
	for href in genre:
		genrename = genrename + href.contents[0] + '/'

	description = soup.find("meta", {"name":"description"})['content']
	description = description.replace("&amp;quot;", "")
	description = description.replace("&amp;ndash;", "")
	description = description.replace("&#039;", "")
	description = description.replace("&amp&amp", "")
	description = description.replace("&quot;&ndash", "")
	description = description.replace("&ndash;", "")
	description = description.replace('\n', "")
	print (gamename)
	gamefile = number + '.txt'
	with open(gamefile, 'w+') as f:
		f.write(gamename +'#'+ players + '#' + ages + " and up" + '#' + time + '#' + genrename + '#' + description)
		f.close()
