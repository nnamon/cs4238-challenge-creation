# SOLUTION

First, find the hidden file. `ls -a` won't work because it's not the real `ls`.
Instead, use `find` to find all files in the home directory.

```
$ find -name *.*
.
./.gdbinit
./docs/instructions.md
./docs/solution.md
./docs/hints.md
./.bash_logout
./.bashrc
./.password
./.profile
```

`.password` is there. Next, use the absolute path to execute `cat`.

```
/bin/cat .password
```
