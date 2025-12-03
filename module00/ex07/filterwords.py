import sys
import re

argv = sys.argv[1:]
if len(argv) != 2:
    print("ERROR")
    sys.exit()

S = argv[0]
if not isinstance(S, str):
    print("ERROR")
    sys.exit()

try:
    N = int(argv[1])
except ValueError:
    print("ERROR")
    sys.exit()

result = [
    w for w in re.split(r'[\W_]+', S)
    if sum(1 for c in w if c.isprintable) > N
]

print(result)
