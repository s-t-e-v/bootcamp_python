import sys

args = sys.argv[1:]
nb_args = len(args)
if nb_args == 0:
    print(f"""\
Usage: python operations.py <number1> <number2>
Example:
    python operations.py 10 3""")
    sys.exit()
elif nb_args == 1:
    print("AssertionError: two arguments are required")
    sys.exit()
elif nb_args > 2:
    print("AssertionError: too many arguments")
    sys.exit()

try:
    a = int(args[0])
    b = int(args[1])
except ValueError:
    print("AssertionError: only integers")
    sys.exit()

result = {}
result["sum"] = a + b
result["difference"] = a - b
result["product"] = a * b
try:
    result["quotient"] = a / b
except ZeroDivisionError:
    result["quotient"] = "ERROR (division by zero)"
try:
    result["remainder"] = a % b
except ZeroDivisionError:
    result["remainder"] = "ERROR (modulo by zero)"


print(f"""\
    Sum:        {result['sum']}
    Difference: {result['difference']}
    Product:    {result['product']}
    Quotient:   {result['quotient']}
    Remainder:  {result['remainder']}""")
