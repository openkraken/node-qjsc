# node-qjsc
Node.js addon for the Quickjs compiler

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

// Evaluate bytecode in quickjs engine directly.
qjsc.evalByteCode(buffer);
```

## Contribute

**Generate compile_commands.json**

```
node-gyp configure -- -f gyp.generator.compile_commands_json.py
```
