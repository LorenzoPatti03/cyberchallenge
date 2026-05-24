import requests

s = requests.Session()
url1 = 'http://web-11.challs.olicyber.it/login'
url2 = 'http://web-11.challs.olicyber.it/flag_piece'

r1 = s.post(url1, json={"username": "admin", "password": "admin"})
data = r1.json()

csrf = data.get('csrf')
session_id = s.cookies.get('session')
flag = []
for i in range(0,4):
    params = {
        'csrf': csrf,
        'index': i
    }

    cookies = {
        'session': session_id
    }

    respond = s.get(url2, params=params, cookies=cookies)
    data = respond.json()
    csrf = data.get("csrf")
    flag.append( data.get("flag_piece"))
    print(respond.content)

print("".join(flag))