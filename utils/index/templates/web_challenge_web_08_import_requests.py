import requests


s = requests.Session()
url = 'http://web-08.challs.olicyber.it/login'
dati_form = {
    'username': 'admin',
    'password': 'admin'
}
responde = s.post(url,data=dati_form)
print(responde.content)