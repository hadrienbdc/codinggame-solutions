import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
f = []
b = []
fb = []
start = None


def pgcd(a, b):
    while a % b != 0:
        a, b = b, a % b
    return b


for i in range(n):
    line = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

    if "Fizz" in line:
        f.append(i)
    if "Buzz" in line:
        b.append(i)

    if not start:
        if line.isdigit():
            start = int(line) - i

if not start:
    start = 1

if len(f) > 1:
    f = pgcd(int(f[0]) + start, int(f[1]) + start)
else:
    f = int(f[0]) + start

if len(b) > 1:
    b = pgcd(int(b[0]) + start, int(b[1]) + start)
else:
    b = int(b[0]) + start

print(f"{f} {b}")
