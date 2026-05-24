import requests 

s = requests.Session()
url1 = 'http://web-06.challs.olicyber.it/token'
url2= 'http://web-06.challs.olicyber.it/flag'
s.get(url1)
responde = s.get(url2)
print(responde.content)