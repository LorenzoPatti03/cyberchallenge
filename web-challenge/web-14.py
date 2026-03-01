import requests
from bs4 import BeautifulSoup,Comment

s = requests.Session()
url = 'http://web-14.challs.olicyber.it/'
respond = s.get(url)
soup = BeautifulSoup(respond.content, 'html.parser')
#print(soup)

commenti = soup.find_all(string=lambda text: isinstance(text, Comment))
'''
Questa è la parte più importante. In una pagina HTML, BeautifulSoup classifica i pezzi di testo in diversi modi:

    NavigableString: Il testo normale che leggi sulla pagina (es. "Lorem Ipsum").

    Comment: Il testo nascosto tra ``.

isinstance(text, Comment) restituisce True solo se quel pezzetto di testo è un commento. Se è testo normale, restituisce False e viene scartato.'''
for c in commenti:
    print(f"Commento trovato: {c.strip()}")


