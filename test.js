const Qjsc = require('./index');

const qjsc = new Qjsc();

describe('qjsc', () => {
  it('throw error when empty arguments', () => {
    expect(() => qjsc.compile()).toThrowError('1st arguments should be string.');
  });

  it('throw error when js syntax not correct', () => {
    const code = `
    function f() {

    console.log(111;

    `;
    expect(() => qjsc.compile(code)).toThrowError();
  });

  it('return bytecode binary', () => {
    const code = `
    function f() { return 1 + '1234'; }
    f();
    `;
    let buffer = qjsc.compile(code);
    expect(qjsc._evalByteCode(buffer)).toBe('11234');
  });

  it('support 20210327', () => {
    expect(qjsc.version).toBe('20210327');
  });

  it('get all supported version', () => {
    expect(qjsc.getSupportedVersions()).toEqual(['20210327']);
  });
});
