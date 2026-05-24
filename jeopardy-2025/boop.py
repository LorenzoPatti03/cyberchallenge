


import requests


url ='http://boop.challs.cyberchallenge.it/'

responde = requests.get(url)
print(responde.text)