import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin # Strumento fondamentale per unire gli URL

s = requests.Session()
url = 'http://web-16.challs.olicyber.it/'
respond = s.get(url)
soup = BeautifulSoup(respond.text, 'html.parser')
visited = set()


risorse = soup.find_all('a')
links = [risorsa.get('href') for risorsa in risorse]

for path in links:
    url_completo = urljoin(url, path)
    if path in visited:
        continue
    visited.add(path)
    respond = s.get(url_completo)
    soup = BeautifulSoup(respond.text, 'html.parser')
    risorse = soup.find_all('a')
    tmp = [risorsa.get('href') for risorsa in risorse]
    links += tmp
    titoli = soup.find_all('h1')

    for h1 in titoli:
        # Applica la regex sul testo contenuto nel tag
        match = re.search(r'flag\{.*?\}', h1.get_text())
        if match:
            print(f"Flag trovata nell'H1: {match.group()}")