# [web - nWAF](https://hack.cert.pl/challenge/nWAF)

The main vulnerability is in the *random* JWT secret that is generated like this: `random.randint(2 ^ 127, 2 ^ 128).to_bytes(16, 'big')`. In Python, `^` is an XOR operator, not power, so the range is `(125, 130)`, which is easy to guess. Knowing the secret, you can make the challenge's server return anything since it renders the username in the `/hello` endpoint. If the middleware detects the correct part of the flag in the response, it returns 401. This way, you can guess parts of the flag as it is done in `sol.py`.

### Flag
```
ecsc24{mowa_jest_srebrem_a_milczenie_owiec!}
```