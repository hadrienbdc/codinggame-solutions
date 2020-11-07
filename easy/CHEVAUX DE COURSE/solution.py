import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
all_p = []
for i in range(n):
    pi = int(input())
    all_p.append(pi)

all_p = sorted(all_p)
min_diff = 10000
for i in range(n-1):
    diff = all_p[i+1] - all_p[i]
    min_diff = min(min_diff, diff)

print(min_diff)
