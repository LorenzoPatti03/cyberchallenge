import requests

#payload = {"X-Password": 'admin'}
#headers = {'Accept': 'application/xml'}
url = 'http://web-05.challs.olicyber.it/flag'
sfida_cookies = {'password': 'admin'}
responde = requests.get(url,cookies=sfida_cookies)
print(responde.content)