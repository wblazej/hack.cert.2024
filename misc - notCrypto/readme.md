# [misc - notCrypto](https://hack.cert.pl/challenge/notCrypto)

Method `secrets` generates random uuid for every character, except the `Character.MAX_VALUE`, since the range's closing value is not included. That's why for 11 characters long seed which consits of only characters `65535` the encryption key will always be the same.

#### Generate proper output
```py
from pwn import remote

c = remote('notcrypto.ecsc24.hack.cert.pl', 5103)
c.sendline(''.join(chr(65535) for _ in range(11)).encode())
res = c.recv().decode().strip()
print(res)
```

Then decrypt the flag with `sol.java`.

### Flag
```
ecsc24{integer_cache_and_2_byte_chars_#justjavathings}
```