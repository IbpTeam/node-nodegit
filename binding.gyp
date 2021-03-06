{
  "targets": [
    {
      "target_name": "nodegit",

      "dependencies": [
        "libgit2"
      ],

      "sources": [
        "src/base.cc",
        "src/blob.cc",
        "src/commit.cc",
        "src/oid.cc",
        "src/reference.cc",
        "src/object.cc",
        "src/repo.cc",
        "src/index.cc",
        "src/index_entry.cc",
        "src/index_time.cc",
        "src/tag.cc",
        "src/revwalk.cc",
        "src/signature.cc",
        "src/time.cc",
        "src/tree.cc",
        "src/tree_builder.cc",
        "src/tree_entry.cc",
        "src/diff_find_options.cc",
        "src/diff_options.cc",
        "src/diff_list.cc",
        "src/patch.cc",
        "src/delta.cc",
        "src/diff_file.cc",
        "src/diff_range.cc",
        "src/threads.cc",
        "src/wrapper.cc",
        "src/refdb.cc",
        "src/odb_object.cc",
        "src/odb.cc",
        "src/submodule.cc",
        "src/remote.cc",
        "src/clone_options.cc",
        "src/functions/copy.cc",
      ],

      "include_dirs": [
        "vendor/libv8-convert",
        "vendor/libgit2/include",
        "<!(node -e \"require('nan')\")"
      ],

      "cflags": [
        "-Wall",
      ],

      "conditions": [
        [
          "OS=='mac'", {
            "xcode_settings": {
              "GCC_ENABLE_CPP_EXCEPTIONS": "YES",

              "WARNING_CFLAGS": [
                "-Wno-unused-variable",
              ],
            }
          }
        ]
      ]
    },
    {
      "target_name": "libgit2",
      "type": "static_library",
      "defines": [
        "GIT_THREADS",
        # Node's util.h may be accidentally included so use this to guard
        # against compilation error.
        "SRC_UTIL_H_",
      ],
      "dependencies": [
        "zlib",
        "http_parser",
      ],
      "sources": [
        "vendor/libgit2/src/attr.c",
        "vendor/libgit2/src/attr.h",
        "vendor/libgit2/src/attr_file.c",
        "vendor/libgit2/src/attr_file.h",
        "vendor/libgit2/src/blob.c",
        "vendor/libgit2/src/blob.h",
        "vendor/libgit2/src/branch.c",
        "vendor/libgit2/src/branch.h",
        "vendor/libgit2/src/bswap.h",
        "vendor/libgit2/src/buf_text.c",
        "vendor/libgit2/src/buf_text.h",
        "vendor/libgit2/src/buffer.c",
        "vendor/libgit2/src/buffer.h",
        "vendor/libgit2/src/cache.c",
        "vendor/libgit2/src/cache.h",
        "vendor/libgit2/src/cc-compat.h",
        "vendor/libgit2/src/checkout.c",
        "vendor/libgit2/src/checkout.h",
        "vendor/libgit2/src/clone.c",
        "vendor/libgit2/src/commit.c",
        "vendor/libgit2/src/commit.h",
        "vendor/libgit2/src/commit_list.c",
        "vendor/libgit2/src/commit_list.h",
        "vendor/libgit2/src/common.h",
        "vendor/libgit2/src/compress.c",
        "vendor/libgit2/src/compress.h",
        "vendor/libgit2/src/config.c",
        "vendor/libgit2/src/config.h",
        "vendor/libgit2/src/config_cache.c",
        "vendor/libgit2/src/config_file.c",
        "vendor/libgit2/src/config_file.h",
        "vendor/libgit2/src/crlf.c",
        "vendor/libgit2/src/date.c",
        "vendor/libgit2/src/delta-apply.c",
        "vendor/libgit2/src/delta-apply.h",
        "vendor/libgit2/src/delta.c",
        "vendor/libgit2/src/delta.h",
        "vendor/libgit2/src/diff.c",
        "vendor/libgit2/src/diff.h",
        "vendor/libgit2/src/diff_output.c",
        "vendor/libgit2/src/diff_output.h",
        "vendor/libgit2/src/diff_tform.c",
        "vendor/libgit2/src/errors.c",
        "vendor/libgit2/src/fetch.c",
        "vendor/libgit2/src/fetch.h",
        "vendor/libgit2/src/fetchhead.c",
        "vendor/libgit2/src/fetchhead.h",
        "vendor/libgit2/src/filebuf.c",
        "vendor/libgit2/src/filebuf.h",
        "vendor/libgit2/src/fileops.c",
        "vendor/libgit2/src/fileops.h",
        "vendor/libgit2/src/filter.c",
        "vendor/libgit2/src/filter.h",
        "vendor/libgit2/src/fnmatch.c",
        "vendor/libgit2/src/fnmatch.h",
        "vendor/libgit2/src/global.c",
        "vendor/libgit2/src/global.h",
        "vendor/libgit2/src/graph.c",
        "vendor/libgit2/src/hash.c",
        "vendor/libgit2/src/hash.h",
        "vendor/libgit2/src/hashsig.c",
        "vendor/libgit2/src/hashsig.h",
        "vendor/libgit2/src/ignore.c",
        "vendor/libgit2/src/ignore.h",
        "vendor/libgit2/src/index.c",
        "vendor/libgit2/src/index.h",
        "vendor/libgit2/src/indexer.c",
        "vendor/libgit2/src/iterator.c",
        "vendor/libgit2/src/iterator.h",
        "vendor/libgit2/src/khash.h",
        "vendor/libgit2/src/map.h",
        "vendor/libgit2/src/merge.c",
        "vendor/libgit2/src/merge.h",
        "vendor/libgit2/src/message.c",
        "vendor/libgit2/src/message.h",
        "vendor/libgit2/src/mwindow.c",
        "vendor/libgit2/src/mwindow.h",
        "vendor/libgit2/src/netops.c",
        "vendor/libgit2/src/netops.h",
        "vendor/libgit2/src/notes.c",
        "vendor/libgit2/src/notes.h",
        "vendor/libgit2/src/object.c",
        "vendor/libgit2/src/object.h",
        "vendor/libgit2/src/odb.c",
        "vendor/libgit2/src/odb.h",
        "vendor/libgit2/src/odb_loose.c",
        "vendor/libgit2/src/odb_pack.c",
        "vendor/libgit2/src/offmap.h",
        "vendor/libgit2/src/oid.c",
        "vendor/libgit2/src/oidmap.h",
        "vendor/libgit2/src/pack-objects.c",
        "vendor/libgit2/src/pack-objects.h",
        "vendor/libgit2/src/pack.c",
        "vendor/libgit2/src/pack.h",
        "vendor/libgit2/src/path.c",
        "vendor/libgit2/src/path.h",
        "vendor/libgit2/src/pathspec.c",
        "vendor/libgit2/src/pathspec.h",
        "vendor/libgit2/src/pool.c",
        "vendor/libgit2/src/pool.h",
        "vendor/libgit2/src/posix.c",
        "vendor/libgit2/src/posix.h",
        "vendor/libgit2/src/pqueue.c",
        "vendor/libgit2/src/pqueue.h",
        "vendor/libgit2/src/push.c",
        "vendor/libgit2/src/push.h",
        "vendor/libgit2/src/refdb.c",
        "vendor/libgit2/src/refdb.h",
        "vendor/libgit2/src/refdb_fs.c",
        "vendor/libgit2/src/refdb_fs.h",
        "vendor/libgit2/src/reflog.c",
        "vendor/libgit2/src/reflog.h",
        "vendor/libgit2/src/refs.c",
        "vendor/libgit2/src/refs.h",
        "vendor/libgit2/src/refspec.c",
        "vendor/libgit2/src/refspec.h",
        "vendor/libgit2/src/remote.c",
        "vendor/libgit2/src/remote.h",
        "vendor/libgit2/src/repo_template.h",
        "vendor/libgit2/src/repository.c",
        "vendor/libgit2/src/repository.h",
        "vendor/libgit2/src/reset.c",
        "vendor/libgit2/src/revparse.c",
        "vendor/libgit2/src/revwalk.c",
        "vendor/libgit2/src/revwalk.h",
        "vendor/libgit2/src/sha1_lookup.c",
        "vendor/libgit2/src/sha1_lookup.h",
        "vendor/libgit2/src/signature.c",
        "vendor/libgit2/src/signature.h",
        "vendor/libgit2/src/stash.c",
        "vendor/libgit2/src/status.c",
        "vendor/libgit2/src/strmap.h",
        "vendor/libgit2/src/submodule.c",
        "vendor/libgit2/src/submodule.h",
        "vendor/libgit2/src/tag.c",
        "vendor/libgit2/src/tag.h",
        "vendor/libgit2/src/thread-utils.c",
        "vendor/libgit2/src/thread-utils.h",
        "vendor/libgit2/src/trace.c",
        "vendor/libgit2/src/trace.h",
        "vendor/libgit2/src/transport.c",
        "vendor/libgit2/src/tree-cache.c",
        "vendor/libgit2/src/tree-cache.h",
        "vendor/libgit2/src/tree.c",
        "vendor/libgit2/src/tree.h",
        "vendor/libgit2/src/tsort.c",
        "vendor/libgit2/src/util.c",
        "vendor/libgit2/src/util.h",
        "vendor/libgit2/src/vector.c",
        "vendor/libgit2/src/vector.h",
        "vendor/libgit2/src/transports/cred.c",
        "vendor/libgit2/src/transports/cred_helpers.c",
        "vendor/libgit2/src/transports/git.c",
        "vendor/libgit2/src/transports/http.c",
        "vendor/libgit2/src/transports/local.c",
        "vendor/libgit2/src/transports/smart.c",
        "vendor/libgit2/src/transports/smart.h",
        "vendor/libgit2/src/transports/smart_pkt.c",
        "vendor/libgit2/src/transports/smart_protocol.c",
        "vendor/libgit2/src/xdiff/xdiff.h",
        "vendor/libgit2/src/xdiff/xdiffi.c",
        "vendor/libgit2/src/xdiff/xdiffi.h",
        "vendor/libgit2/src/xdiff/xemit.c",
        "vendor/libgit2/src/xdiff/xemit.h",
        "vendor/libgit2/src/xdiff/xhistogram.c",
        "vendor/libgit2/src/xdiff/xinclude.h",
        "vendor/libgit2/src/xdiff/xmacros.h",
        "vendor/libgit2/src/xdiff/xmerge.c",
        "vendor/libgit2/src/xdiff/xpatience.c",
        "vendor/libgit2/src/xdiff/xprepare.c",
        "vendor/libgit2/src/xdiff/xprepare.h",
        "vendor/libgit2/src/xdiff/xtypes.h",
        "vendor/libgit2/src/xdiff/xutils.c",
        "vendor/libgit2/src/xdiff/xutils.h",
        "vendor/libgit2/src/hash/hash_generic.c",
        "vendor/libgit2/src/hash/hash_generic.h",
        "vendor/libgit2/src/hash/hash_openssl.h",
      ],
      "conditions": [
        ["OS=='linux'", {
          "cflags": [
            "-w",
          ],
        }],
        ["OS=='win'", {
          "msvs_settings": {
            "VCLinkerTool": {
              "AdditionalDependencies": [
                "ws2_32.lib",
              ],
            },
            # Workaround of a strange bug:
            # TargetMachine + static_library + x64 = nothing.
            "conditions": [
              ["target_arch=='x64'", {
                "VCLibrarianTool": {
                  "AdditionalOptions": [
                    "/MACHINE:X64",
                  ],
                },
              }, {
                "VCLibrarianTool": {
                  "AdditionalOptions": [
                    "/MACHINE:x86",
                  ],
                },
              }],
            ],
          },
          "msvs_disabled_warnings": [
            # Conversion from 'ssize_t' to 'int32_t', possible loss of data.
            4244,
            # Conversion from 'size_t' to 'int', possible loss of data.
            4267,
            # Different 'volatile' qualifiers.
            4090,
            # 'volatile void *' differs in levels of indirection from 'int'.
            4047,
            # 'InterlockedDecrement' undefined; assuming extern returning int.
            4013,
          ],
          "sources": [
            "vendor/libgit2/src/win32/dir.c",
            "vendor/libgit2/src/win32/dir.h",
            "vendor/libgit2/src/win32/error.c",
            "vendor/libgit2/src/win32/error.h",
            "vendor/libgit2/src/win32/findfile.c",
            "vendor/libgit2/src/win32/findfile.h",
            "vendor/libgit2/src/win32/git2.rc",
            "vendor/libgit2/src/win32/map.c",
            "vendor/libgit2/src/win32/mingw-compat.h",
            "vendor/libgit2/src/win32/msvc-compat.h",
            "vendor/libgit2/src/win32/posix.h",
            "vendor/libgit2/src/win32/posix_w32.c",
            "vendor/libgit2/src/win32/precompiled.c",
            "vendor/libgit2/src/win32/precompiled.h",
            "vendor/libgit2/src/win32/pthread.c",
            "vendor/libgit2/src/win32/pthread.h",
            "vendor/libgit2/src/win32/utf-conv.c",
            "vendor/libgit2/src/win32/utf-conv.h",
            "vendor/libgit2/src/win32/version.h",
            "vendor/libgit2/deps/regex/regex.c",
          ],
        }, {
          "libraries": [
            "-lpthread",
          ],
          "sources": [
            "vendor/libgit2/src/unix/map.c",
            "vendor/libgit2/src/unix/posix.h",
            "vendor/libgit2/src/unix/realpath.c",
          ],
          "cflags": [
            "-Wno-missing-field-initializers",
            "-Wno-unused-variable",
            "-Wno-deprecated-declarations",
          ],
          "xcode_settings": {
            "WARNING_CFLAGS": [
              "-Wno-missing-field-initializers",
              "-Wno-unused-variable",
              "-Wno-deprecated-declarations",
              "-Wno-uninitialized",
            ],
          },
        },
      ]
      ],
      "include_dirs": [
        "vendor/libgit2/include",
        "vendor/libgit2/src",
        "vendor/libgit2/deps/regex",
      ],
      "direct_dependent_settings": {
        "include_dirs": [
          "vendor/libgit2/include",
        ],
      },
    },
    {
      "target_name": "zlib",
      "type": "static_library",
      "sources": [
        "vendor/libgit2/deps/zlib/adler32.c",
        "vendor/libgit2/deps/zlib/crc32.c",
        "vendor/libgit2/deps/zlib/crc32.h",
        "vendor/libgit2/deps/zlib/deflate.c",
        "vendor/libgit2/deps/zlib/deflate.h",
        "vendor/libgit2/deps/zlib/inffast.c",
        "vendor/libgit2/deps/zlib/inffast.h",
        "vendor/libgit2/deps/zlib/inffixed.h",
        "vendor/libgit2/deps/zlib/inflate.c",
        "vendor/libgit2/deps/zlib/inflate.h",
        "vendor/libgit2/deps/zlib/inftrees.c",
        "vendor/libgit2/deps/zlib/inftrees.h",
        "vendor/libgit2/deps/zlib/trees.c",
        "vendor/libgit2/deps/zlib/trees.h",
        "vendor/libgit2/deps/zlib/zconf.h",
        "vendor/libgit2/deps/zlib/zlib.h",
        "vendor/libgit2/deps/zlib/zutil.c",
        "vendor/libgit2/deps/zlib/zutil.h",
      ],
      "defines": [
        "NO_VIZ",
        "STDC",
        "NO_GZIP",
      ],
      "include_dirs": [
        "vendor/libgit2/include",
        "vendor/libgit2/deps/regex",
      ],
      "direct_dependent_settings": {
        "include_dirs": [
          "vendor/libgit2/deps/zlib",
        ],
      },
    },
    {
      "target_name": "http_parser",
      "type": "static_library",
      "sources": [
        "vendor/libgit2/deps/http-parser/http_parser.c",
        "vendor/libgit2/deps/http-parser/http_parser.h",
      ],
      "direct_dependent_settings": {
        "include_dirs": [
          "vendor/libgit2/deps/http-parser",
        ],
      },
      "conditions": [
        ["OS=='win'", {
          "msvs_disabled_warnings": [
            # Conversion from 'ssize_t' to 'int32_t', possible loss of data.
            4244,
          ],
        }],
      ],
    },
  ]
}
