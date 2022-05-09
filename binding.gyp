{
  "targets": [
    {
      "target_name": "qjsc_20210327",
      "sources": [
        "src/qjsc_20210327.cc",
        "deps/quickjs_2021_03_27/cutils.c",
        "deps/quickjs_2021_03_27/cutils.h",
        "deps/quickjs_2021_03_27/libregexp.c",
        "deps/quickjs_2021_03_27/libregexp.h",
        "deps/quickjs_2021_03_27/libregexp-opcode.h",
        "deps/quickjs_2021_03_27/libunicode.c",
        "deps/quickjs_2021_03_27/libunicode.h",
        "deps/quickjs_2021_03_27/libunicode-table.h",
        "deps/quickjs_2021_03_27/list.h",
        "deps/quickjs_2021_03_27/quickjs.c",
        "deps/quickjs_2021_03_27/quickjs.h",
        "deps/quickjs_2021_03_27/quickjs-atom.h",
        "deps/quickjs_2021_03_27/quickjs-opcode.h",
      ],
      'include_dirs': [
        "<!(node -p \"require('node-addon-api').include_dir\")",
        "pthreads"
      ],
      "defines": [
        'CONFIG_VERSION=\"2021-03-27\"'
      ],
      'cflags!': [ '-fexceptions' ],
      'cflags_cc!': [ '-fexceptions', ],
      'cflags': [ '-Wno-sign-compare' ],
      'conditions': [
        ["OS=='win'", {
          "defines": [
            "_HAS_EXCEPTIONS=1",
            "HAVE_STRUCT_TIMESPEC=1"
          ],
          "msvs_settings": {
            "VCCLCompilerTool": {
              "ExceptionHandling": 1
            },
          },
        }],
        ["OS=='linux'", {
          'cflags_cc': ['-fvisibility=hidden'],
          "defines": [
            "NAPI_DISABLE_CPP_EXCEPTIONS"
          ],
        }],
        ["OS=='mac'", {
          'cflags_cc': ['-fvisibility=hidden'],
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'CLANG_CXX_LIBRARY': 'libc++',
            'MACOSX_DEPLOYMENT_TARGET': '10.7',
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
            "OTHER_CFLAGS": [ '-Wno-sign-compare' ],
          },
        }],
  ],
    }
  ]
}
