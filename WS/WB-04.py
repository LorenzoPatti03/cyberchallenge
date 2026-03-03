import requests

url ='https://use.fontawesome.com/releases/v5.3.1/js/all.js'

respond = requests.get(url)
print(respond.text)
print(respond.headers)