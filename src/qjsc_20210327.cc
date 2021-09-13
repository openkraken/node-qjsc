#include <napi.h>
#include "../deps/quickjs_2021_03_27/quickjs.h"

static void reportError(Napi::Env &env, JSContext *ctx, JSValue error) {
  const char *title = JS_ToCString(ctx, error);
  const char *stack = nullptr;
  JSValue stackValue = JS_GetPropertyStr(ctx, error, "stack");
  if (!JS_IsUndefined(stackValue)) {
    stack = JS_ToCString(ctx, stackValue);
  }

  uint32_t messageLength = strlen(title) + 2;
  if (stack != nullptr) {
    messageLength += strlen(stack);
    char message[messageLength];
    sprintf(message, "%s\n%s", title, stack);
    Napi::TypeError::New(env, message).ThrowAsJavaScriptException();
  } else {
    char message[messageLength];
    sprintf(message, "%s", title);
    Napi::TypeError::New(env, message).ThrowAsJavaScriptException();
  }

};

/// Convert javascript source code to quickjs bytecode.
Napi::Value DumpByteCode(const Napi::CallbackInfo &info) {
  Napi::Env env = info.Env();

  if (info.Length() < 2) {
    Napi::TypeError::New(env, "2 arguments required").ThrowAsJavaScriptException();
    return env.Null();
  }

  if (!info[0].IsString()) {
    Napi::TypeError::New(env, "1st arguments should be string.").ThrowAsJavaScriptException();
    return env.Null();
  }

  if (!info[1].IsString()) {
    Napi::TypeError::New(env, "2st arguments should be string.").ThrowAsJavaScriptException();
    return env.Null();
  }

  JSRuntime *runtime = JS_NewRuntime();
  JSContext *ctx = JS_NewContext(runtime);

  std::string code = info[0].As<Napi::String>().Utf8Value();
  std::string sourceUrl = info[1].As<Napi::String>().Utf8Value();

  JSValue object = JS_Eval(ctx, code.c_str(), code.size(), sourceUrl.c_str(),
                           JS_EVAL_TYPE_GLOBAL | JS_EVAL_FLAG_COMPILE_ONLY);
  if (JS_IsException(object)) {
    JSValue error = JS_GetException(ctx);
    reportError(env, ctx, error);
    return env.Null();
  }

  size_t byteCodeLength;
  uint8_t *bytes = JS_WriteObject(ctx, &byteCodeLength, object, JS_WRITE_OBJ_BYTECODE);
  Napi::Buffer<uint8_t> buffer = Napi::Buffer<uint8_t>::New(env, bytes, byteCodeLength);

  JS_FreeValue(ctx, object);
  JS_FreeContext(ctx);
  JS_FreeRuntime(runtime);
  return buffer;
}

Napi::Value evalByteCode(const Napi::CallbackInfo &info) {
  Napi::Env env = info.Env();

  if (info.Length() == 0) {
    Napi::TypeError::New(env, "1 arguments required").ThrowAsJavaScriptException();
    return env.Null();
  }

  if (!info[0].IsBuffer()) {
    Napi::TypeError::New(env, "1st arguments must be buffer").ThrowAsJavaScriptException();
    return env.Null();
  }

  JSRuntime *runtime = JS_NewRuntime();
  JSContext *ctx = JS_NewContext(runtime);

  Napi::Buffer<uint8_t> buffer = info[0].As<Napi::Buffer<uint8_t>>();
  uint8_t *bytes = buffer.Data();
  size_t byteLength = buffer.ByteLength();

  JSValue object;
  object = JS_ReadObject(ctx, bytes, byteLength, JS_READ_OBJ_BYTECODE);
  if (JS_IsException(object)) {
    JSValue error = JS_GetException(ctx);
    reportError(env, ctx, error);
    return env.Null();
  }

  JSValue value = JS_EvalFunction(ctx, object);
  if (JS_IsException(value)) {
    JSValue error = JS_GetException(ctx);
    reportError(env, ctx, error);
    return env.Null();
  }

  const char* returnString = JS_ToCString(ctx, value);
  JS_FreeValue(ctx, value);
  Napi::String result = Napi::String::New(env, returnString);
  JS_FreeCString(ctx, returnString);
  JS_FreeContext(ctx);
  JS_FreeRuntime(runtime);
  return result;
}

/**
* This code is our entry-point. We receive two arguments here, the first is the
* environment that represent an independent instance of the JavaScript runtime,
* the second is exports, the same as module.exports in a .js file.
* You can either add properties to the exports object passed in or create your
* own exports object. In either case you must return the object to be used as
* the exports for the module when you return from the Init function.
*/
Napi::Object Init(Napi::Env env, Napi::Object exports) {
  exports.Set(Napi::String::New(env, "dumpByteCode"), Napi::Function::New(env, DumpByteCode));
  exports.Set(Napi::String::New(env, "version"), Napi::String::New(env, "20210327"));
  exports.Set(Napi::String::New(env, "evalByteCode"), Napi::Function::New(env, evalByteCode));
  return exports;
}

/**
* This code defines the entry-point for the Node addon, it tells Node where to go
* once the library has been loaded into active memory. The first argument must
* match the "target" in our *binding.gyp*. Using NODE_GYP_MODULE_NAME ensures
* that the argument will be correct, as long as the module is built with
* node-gyp (which is the usual way of building modules). The second argument
* points to the function to invoke. The function must not be namespaced.
*/
NODE_API_MODULE(NODE_GYP_MODULE_NAME, Init)
