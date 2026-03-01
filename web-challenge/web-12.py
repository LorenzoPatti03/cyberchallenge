import requests
from bs4 import BeautifulSoup


s = requests.Session()
url = ' http://web-12.challs.olicyber.it/'
respond = s.get(url)
soup = BeautifulSoup(respond.content, 'html.parser')
print(soup)