import sys

args = sys.argv[1:]

if len(args) > 1:
    print("AssertionError: more than one argument is provided")
    sys.exit()

if len(args) == 0:
    sys.exit()

try:
    nb = int(args[0])
    if nb == 0:
        print("I'm Zero.")
    elif nb % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")
except ValueError:
    print("AssertionError: argument is not an integer")
