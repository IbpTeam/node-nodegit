cmd_Release/obj.target/nodegit.node := flock ./Release/linker.lock g++ -shared -pthread -rdynamic -m32  -Wl,-soname=nodegit.node -o Release/obj.target/nodegit.node -Wl,--start-group Release/obj.target/nodegit/src/base.o Release/obj.target/nodegit/src/blob.o Release/obj.target/nodegit/src/commit.o Release/obj.target/nodegit/src/oid.o Release/obj.target/nodegit/src/reference.o Release/obj.target/nodegit/src/object.o Release/obj.target/nodegit/src/repo.o Release/obj.target/nodegit/src/index.o Release/obj.target/nodegit/src/index_entry.o Release/obj.target/nodegit/src/index_time.o Release/obj.target/nodegit/src/tag.o Release/obj.target/nodegit/src/revwalk.o Release/obj.target/nodegit/src/signature.o Release/obj.target/nodegit/src/time.o Release/obj.target/nodegit/src/tree.o Release/obj.target/nodegit/src/tree_builder.o Release/obj.target/nodegit/src/tree_entry.o Release/obj.target/nodegit/src/diff_find_options.o Release/obj.target/nodegit/src/diff_options.o Release/obj.target/nodegit/src/diff_list.o Release/obj.target/nodegit/src/patch.o Release/obj.target/nodegit/src/delta.o Release/obj.target/nodegit/src/diff_file.o Release/obj.target/nodegit/src/diff_range.o Release/obj.target/nodegit/src/threads.o Release/obj.target/nodegit/src/wrapper.o Release/obj.target/nodegit/src/refdb.o Release/obj.target/nodegit/src/odb_object.o Release/obj.target/nodegit/src/odb.o Release/obj.target/nodegit/src/submodule.o Release/obj.target/nodegit/src/remote.o Release/obj.target/nodegit/src/clone_options.o Release/obj.target/nodegit/src/functions/copy.o Release/obj.target/git2.a Release/obj.target/zlib.a Release/obj.target/http_parser.a -Wl,--end-group 