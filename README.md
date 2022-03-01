# node-qjsc
> Node.js addon for the [QuickJS](https://github.com/bellard/quickjs) compiler.

Current supported version:
+ 20210327

## Install

```
npm install qjsc --save
```

## Usage

```javascript
const Qjsc = require('qjsc');
const qjsc = new Qjsc();

// Dump bytecode from javascript source;
qjsc.compile('function hello() { return 1 + 1};'); // <Buffer ...>

// Use specified quickjs version
qjsc = new Qjsc({version: '20210327'});

// Get all supported versions.
qjsc.getSupportedVersions();
```

## Contribute

**Generate compile_commands.json**

```
node-gyp configure -- -f gyp.generator.compile_commands_json.py
```

**Prebuild linux binary**

1. Install docker
2. Build local image with Dockerfile
  ```
  docker build -t qjsc .
  ```
3. Enter into images
  ```
  docker run --rm -it -v $(pwd):/project qjsc
  ```
4. Set up env in docker container
  ```
  cd project
  scl enable rh-nodejs12 bash
  scl enable devtoolset-7 bash
  ```
5. Build your binary
  ```
  npm install
  npm run prebuild
  ```
