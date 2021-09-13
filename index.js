const supportedVersion = ['20210327'];

class Qjsc {
  constructor(version = '20210327') {
    if (supportedVersion.indexOf(version) === -1) {
      throw new Error('Unsupported quickjs version: ' + version);
    }
    this._bindings = require('bindings')(`qjsc_${version}.node`);
  }
  help() {
    console.log('supported version: ' + supportedVersion.join(', '));
  }

  getAllSupportedVersion() {
    return supportedVersion;
  }

  dumpByteCode(code, sourceURL = 'internal://') {
    return this._bindings.dumpByteCode(code, sourceURL);
  }

  get version() {
    return this._bindings.version;
  }

  evalByteCode(buffer) {
    return this._bindings.evalByteCode(buffer);
  }
}

module.exports = Qjsc;
