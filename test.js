const Qjsc = require('./index');

const qjsc = new Qjsc();

describe('qjsc', () => {
  it('throw error when empty arguments', () => {
    expect(() => qjsc.dumpByteCode()).toThrowError('1st arguments should be string.');
  });

  it('throw error when js syntax not correct', () => {
    const code = `
    function f() {

    console.log(111;

    `;
    expect(() => qjsc.dumpByteCode(code)).toThrowError();
  });

  it('return bytecode binary', () => {
    const code = `
    function f() { return 1 + '1234'; }
    f();
    `;
    let buffer = qjsc.dumpByteCode(code);
    expect(qjsc.evalByteCode(buffer)).toBe('11234');
  });
});
