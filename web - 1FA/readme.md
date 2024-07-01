# [web - 1FA](https://hack.cert.pl/challenge/1fa)

Surely it is not the intended vulnerability, but still is. The OTP verification endpoint has no rate limiting and the code is 6-digit, which gives `1 000 000` possibilities. Sending `200` random codes per second gives:
- `99.98%` chances of failure after `1 second`
- `~98.807%` chances of failure after `1 minute`
- `~48.67%` chances of failure after `1 hour`
- and `~02.73%` chances of failure after `5 hours`, which gives about `97%` chances of getting the code right

Using `brute.py` I got the code right after 1h 40m. Then replaced response cookie with my cookie and obtained the flag.

### Flag
```
ecsc24{y0u'v3_w0n_7h3_r4c3}
```