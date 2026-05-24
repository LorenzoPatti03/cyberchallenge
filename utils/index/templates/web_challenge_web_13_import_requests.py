import requests
from bs4 import BeautifulSoup


s = requests.Session()
url = '  http://web-13.challs.olicyber.it/'
respond = s.get(url)
soup = BeautifulSoup(respond.content, 'html.parser')
#print(soup)
'''
# Cerca: <span class="red" id="secret">
tags = soup.find_all('span', {'class': 'red', 'id': 'secret'})

# Cerca sia <span> sia <b> con classe red
tags = soup.find_all(['span', 'b'], {'class': 'red'})'''

tags = soup.find_all('span', {'class':'red'})
lettere_evidenziate = [ tag.get_text() for tag in tags]
print("".join(lettere_evidenziate))