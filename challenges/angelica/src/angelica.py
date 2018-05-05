#!/usr/bin/python

import pickle
import sys
import os
import base64
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

art = file("art.ans").read()

def main():
    # :) Daddy made sure you had something in there
    presents = ["A teddy bear"]
    while True:
        print_banner()
        choice = sys.stdin.readline().strip()
        if choice == "1":
            write("\nList of Presents:\n")
            for i in range(len(presents)):
                write("%d. %s\n" % (i+1, presents[i]))
        elif choice == "2":
            write("\nPlease add the present to the pile: ")
            new_present = sys.stdin.readline().strip()
            presents.append(new_present)
        elif choice == "3":
            write("\nHahahaha as if I'd let daddy add this feature in! - Angelica\n")
        elif choice == "4":
            export = base64.encodestring(pickle.dumps(presents))
            write("\nHere are your presents: %s" % export)
        elif choice == "5":
            try:
                write("\nEnter your import: ")
                imp = sys.stdin.readline().strip()
                imp = base64.decodestring(imp)
                presents = pickle.loads(imp)
                write("Imported %d presents!\n" % len(presents))
            except:
                write("\nSomething wrong happened!\n")
        elif choice == "6":
            f = open(os.path.abspath(__file__), "r").read()
            write("========== DEBUGGING ===========" + "\n")
            write(f + "\n")
            write("========== DEBUGGING ===========" + "\n")
        else:
            write("\nInvalid choice!\n")

def print_banner():
    banner = """
Presents Cataloguing System for my Princess
    Select:
        1 - List Presents
        2 - Add Present
        3 - Delete Present
        4 - Export Presents
        5 - Import Presents
    Choice: """
    write(banner)

def write(data):
    sys.stdout.write(data)
    sys.stdout.flush()

if __name__ == "__main__":
    write(art)
    main()
