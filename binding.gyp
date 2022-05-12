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
              "ExceptionHandling": 1,
              'AdditionalOptions': [ '/std:c11', '/Zc:preprocessor', ],
            },
          },
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

            "compat/win32/pthreads/attr.c",
            "compat/win32/pthreads/barrier.c",
            "compat/win32/pthreads/cancel.c",
            "compat/win32/pthreads/cleanup.c",
            "compat/win32/pthreads/condvar.c",
            "compat/win32/pthreads/create.c",
            "compat/win32/pthreads/dll.c",
            "compat/win32/pthreads/exit.c",
            "compat/win32/pthreads/fork.c",
            "compat/win32/pthreads/global.c",
            "compat/win32/pthreads/misc.c",
            "compat/win32/pthreads/mutex.c",
            "compat/win32/pthreads/private.c",
            "compat/win32/pthreads/rwlock.c",
            "compat/win32/pthreads/sched.c",
            "compat/win32/pthreads/semaphore.c",
            "compat/win32/pthreads/spin.c",
            "compat/win32/pthreads/sync.c",
            "compat/win32/pthreads/tsd.c",
            "compat/win32/pthreads/nonportable.c",
            "compat/win32/pthreads/errno.c",
            "compat/win32/pthreads/signal.c",
            "compat/win32/pthreads/autostatic.c",
          ],
          'include_dirs': [
            "<!(node -p \"require('node-addon-api').include_dir\")",
            "compat/win32/pthreads",
            "compat/win32/atomic"
          ],
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
