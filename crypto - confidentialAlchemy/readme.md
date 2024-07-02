# [crypto - confidentialAlchemy](https://hack.cert.pl/challenge/confiAlchemy)

Run it locally with `echo $enc_aes` and `echo $sha512` to get more information about it. You can notice that `$enc_aes` after decoding always starts with `Salted__`:
```bash
echo 'U2FsdGVkX1+3zYkRMaGNT29nFlcUQ7YEQyYFbyYblg8WDFODjZzwUtjCB6dUMxX0Eisijzg8Is9PUcTI8TfLy2mnDitrRNJQZl+fSUKujOg=' | base64 -d

# Salted__?͉1??OogWC?C&o&
#                      S????R???T3?+"?8<"?OQ???7??i?+kD?Pf_?IB???
```
It means it's sure that `$enc_aes` will always start with `U2FsdGVkX1`. `$sha512` contains a 14 characters long `$secret` and sha512 hash of the `$secret`. You get XOR of these two variables, so knowing first 10 characters of `$enc_eas`, you can brute force last 4 characters to get the whole `$secret`. 

You can check if a guessed secret is correct by comparing last 10 characters of sha512 hash of the guessed secret with last 10 characters of server's output, since `$enc_aes` is shorter then `$sha512` so the ending of the `$sha512` stays unchanged after XOR operation:
```py
>>> bytes.fromhex('f11323f60f914e33c291c7d5d7920e614117015c243e4a0c06633257510d0928674b4749794170684061676f03337f070a504f79287c631917725b6b056367404c334d534e625957574773360e7f50014a057e67034f72015117002a6a4e7b6175692735677b054f7c14685e32643063343637393035313966633036393666336236343363663365633930363136')
b"\xf1\x13#\xf6\x0f\x91N3\xc2\x91\xc7\xd5\xd7\x92\x0eaA\x17\x01\\$>J\x0c\x06c2WQ\r\t(gKGIyAph@ago\x033\x7f\x07\nPOy(|c\x19\x17r[k\x05cg@L3MSNbYWWGs6\x0e\x7fP\x01J\x05~g\x03Or\x01Q\x17\x00*jN{aui'5g{\x05O|\x14h^2d0c46790519fc0696f3b643cf3ec90616"
```

#### Brute force `$secret` and restore `$enc_aes`:
```py
from hashlib import sha512
import itertools
from string import printable

x = bytes.fromhex('f11323f60f914e33c291c7d5d7920e614117015c243e4a0c06633257510d0928674b4749794170684061676f03337f070a504f79287c631917725b6b056367404c334d534e625957574773360e7f50014a057e67034f72015117002a6a4e7b6175692735677b054f7c14685e32643063343637393035313966633036393666336236343363663365633930363136')

base64_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
_all = 64 ** 4
count = 0

for comb in itertools.product(base64_chars, repeat=4):
    a = 'U2FsdGVkX1' + ''.join(comb)
    count += 1

    if count % 100000 == 0:
        print(f'{count}/{_all}')

    secret = bytes([ord(c1) ^ c2 for c1, c2 in zip(a, x)])
    _hash = sha512(secret).hexdigest()

    if _hash[-10:] == x[-10:].decode():
        encrypted = ''.join([chr(c1 ^ c2) for c1, c2 in zip(x, secret + _hash.encode())])
        encrypted = ''.join(l for l in filter(lambda x: x in printable, encrypted))

        print('secret:', secret)
        print('encrypted:', encrypted)

        open('secret.bin', 'wb').write(secret)
        open('encrypted', 'w').write(encrypted)
        exit()
```

#### Decrypt `$enc_aes` to get the flag:
```bash
openssl enc -d -aes-256-cbc -pbkdf2 -iter 1000001 -salt -a -A -kfile secret.bin -in encrypted -out decrypted && cat decrypted
```

### Flag
```
ecsc24{Flag__MoreCryptoMoreSecure!!!!111oneone}
```