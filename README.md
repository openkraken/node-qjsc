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
qjsc.dumpByteCode('function hello() { return 1 + 1};'); // <Buffer ...>

// Use specified quickjs version
qjsc = new Qjsc('20210327');

// Get all supported versions.
qjsc.getAllSupportedVersion();

// Evaluate bytecode in quickjs engine directly.
qjsc.evalByteCode(buffer);
```

## Contribute

**Generate compile_commands.json**

```
node-gyp configure -- -f gyp.generator.compile_commands_json.py
```
