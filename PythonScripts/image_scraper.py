from urllib.request import urlopen
from bs4 import BeautifulSoup

# url = "http://courses.washington.edu/englhtml/engl569/berger/"
# url = "http://courses.washington.edu/englhtml/engl569/berger/Illustrations%20for%20John%20Berger's%20Ways%20of%20Seeing,%20p.%202.html"
url = "http://courses.washington.edu/englhtml/engl569/berger/Illustrations%20for%20John%20Berger's%20Ways%20of%20Seeing,%20p.%203.html"
page = urlopen(url)

soup = BeautifulSoup(page, 'html.parser')

centers = soup.find_all('center')

filename = "image_links.txt"
file = open(filename, 'a')

for center in centers: 
	links = center.find_all('a')
	for link in links:
		file.write(link.get('href'))
		file.write('\n')

file.close()

