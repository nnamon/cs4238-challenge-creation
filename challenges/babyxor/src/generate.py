#!/usr/bin/python

KEY = 0x42

def main():
    password = file("../password").read()
    password = "This is the decrypted password to the next level: " + password
    encrypted = "".join(map(lambda x: chr(ord(x) ^ KEY), password))
    file("./encrypted", 'w').write(encrypted)

if __name__ == "__main__":
    main()
