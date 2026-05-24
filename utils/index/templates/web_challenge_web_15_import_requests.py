import requests
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin # Strumento fondamentale per unire gli URL

s = requests.Session()
url = 'http://web-15.challs.olicyber.it/'
respond = s.get(url)
soup = BeautifulSoup(respond.text, 'html.parser')

# 1. Troviamo TUTTI i tag link (per CSS) e script (per JS)
# Passiamo una lista a find_all per prenderli entrambi in un colpo solo
risorse = soup.find_all(['link', 'script'])

for tag in risorse:
    # 2. Estraiamo l'URL. I link usano 'href', gli script usano 'src'
    percorso = tag.get('href') or tag.get('src')
    
    if percorso:
        # urljoin gestisce da solo se il percorso inizia con / o no
        url_completo = urljoin(url, percorso)
        
        try:
            res_esterna = s.get(url_completo)
            
            # 3. Cerchiamo la flag intera (non solo l'inizio)
            # flag\{.*?\} cerca flag{ seguito da tutto fino alla graffa chiusa
            match = re.search(r'flag\{.*?\}', res_esterna.text)
            
            if match:
                print(f"--- TROVATA in: {url_completo} ---")
                print(f"FLAG: {match.group()}")
            else:
                print(f"Niente in: {url_completo}")
                
        except Exception as e:
            print(f"Errore nello scaricare {url_completo}: {e}")