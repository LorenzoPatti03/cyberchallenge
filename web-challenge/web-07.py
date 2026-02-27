import requests


s = requests.Session()
url = 'http://web-07.challs.olicyber.it/'
responde = s.head(url)
print(responde.headers)