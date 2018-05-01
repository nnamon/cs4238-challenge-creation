#!/usr/bin/python

import sys
import os
import struct

# Change to the current script directory
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

FLAG = open("password").read()
ART = open("art.ansi").read()
KEY = os.urandom(len(FLAG))
STATIC_CONSTANT1 = 0xdeadbeef
STATIC_CONSTANT2 = 0xcafebabe
STATIC_CONSTANT3 = 0xfeedface

def write(data, endl="\n"):
    sys.stdout.write(data + endl)
    sys.stdout.flush()

def readline():
    return sys.stdin.readline()

def main():
    encrypted_flag = ""
    for i in range(len(FLAG)):
        encrypted_flag += chr(ord(FLAG[i]) ^ ord(KEY[i]))

    write(ART)

    write("Welcome to your introduction to Pwntools!")

    write("To begin with, please tell me your name: ", endl="")
    name = readline().strip()
    if name != "Nikolas":
        write("Sorry, you're not the right one!")
        return

    write("Now, give me the first secret key.")
    key1 = sys.stdin.read(4)
    key1_number = struct.unpack("I", key1)[0]
    if key1_number != STATIC_CONSTANT1:
        write("That's wrong!")
        return

    write("Great! Now, give me the second secret key.")
    key2 = sys.stdin.read(4)
    key2_number = struct.unpack("I", key2)[0]
    if key2_number != STATIC_CONSTANT2:
        write("That's wrong!")
        return

    write("Awesome! One more to go.")
    key3 = sys.stdin.read(4)
    key3_number = struct.unpack("I", key3)[0]
    if key3_number != STATIC_CONSTANT3:
        write("That's wrong!")
        return

    write("You did it!")
    write("Here is your decryption key: 0x%s" % KEY.encode("hex"))
    write("Here is your flag: 0x%s" % encrypted_flag.encode("hex"))

if __name__ == "__main__":
    main()
