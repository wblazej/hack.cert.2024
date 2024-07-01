# [web - S69](https://hack.cert.pl/challenge/s69)

In the `/about` page, the IP address field has an XSS vulnerability. Moreover, its value is set with a GET request, so you can inject JavaScript code in the URL. Then you can use the incident report form to make the server enter the malicious URL and leak the access token stored in cookies, as it's done in `sol.py`.

### Flag
```
ecsc24{gotta_have_an_xss_challenge_right?}
```