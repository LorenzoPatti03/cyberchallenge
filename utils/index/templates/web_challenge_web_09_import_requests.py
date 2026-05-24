import requests


s = requests.Session()
url = 'http://web-10.challs.olicyber.it/'
payload = {"username": "admin" , "password": "admin",}
responde = s.patch(url)
print(responde.headers)
