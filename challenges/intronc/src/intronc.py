#!/usr/bin/python

import sys

FLAG = "V4st_oc3ans_0f_truth"

def write(data, endl="\n"):
    sys.stdout.write(data + endl)
    sys.stdout.flush()

def readline():
    return sys.stdin.readline()

def main():
    write("What fell on Issac Newton's head?")
    data = readline()
    if "apple" in data:
        write("That's right! Here's your password: %s" % FLAG)
    else:
        write("That's incorrect!")

if __name__ == "__main__":
    main()
