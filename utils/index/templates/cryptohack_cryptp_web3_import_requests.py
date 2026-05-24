import requests 
import jwt


plain_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImxhIiwiYWRtaW4iOmZhbHNlfQ.jg-TPmp0cg_Jb1pKMXk3Nt--AjCZM6TsPsbA_E67kCc'
url = 'https://web.cryptohack.org/jwt-secrets/authorise/'

session = requests.Session()


encoded = jwt.encode({'username': 'la', 'admin': True}, 'secret', algorithm='HS256')

r = session.get(url + encoded)
print(r.text)
