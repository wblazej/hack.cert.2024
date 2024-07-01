# [web - Board](https://hack.cert.pl/challenge/board)

In a new post, you can put a video link that is opened by the server. You can put, for example, a [webhook.site](https://webhook.site/) URL to reveal the server's IP address, which is not possible any other way since it's a Tor website. Then, simply get `/flag` using the server's IP directly.

```bash
curl 'http://209.38.244.39/flag/'
```

### Flag
```
ecsc24{GreetingsPeopleOfTheWorld-WeWereAnonymous}
```