import sys

args = sys.argv

result = ' '.join(args[1:])[::-1].swapcase()

print(result)
