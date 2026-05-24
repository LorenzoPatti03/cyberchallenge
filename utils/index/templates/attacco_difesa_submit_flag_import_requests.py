import requests

TEAM_TOKEN = '4242424242424242'

flags = ['AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=', 'BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB=']

print(requests.put('http://10.10.0.1:8080/flags', headers={
    'X-Team-Token': TEAM_TOKEN
}, json=flags).text)