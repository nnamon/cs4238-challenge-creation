# SOLUTION

The file `--help` can be read by referring to it by its location, either by full path

```sh
cat /home/introduction/--help
```

or relative

```sh
cat ./--help
```

Alternatively, you can use the end of options flag (`--`) to mark where the options end and the command line args begin

```sh
cat -- --help
```
