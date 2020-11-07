import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
t_list = []
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    t_list.append([t, abs(t)])

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
result = 0
if t_list:
    sorted_t_list = sorted(t_list, key=lambda x: x[1])
    if len(t_list) > 1:
        if sorted_t_list[0][1] == sorted_t_list[1][1]:
            result = max(sorted_t_list[0][0], sorted_t_list[1][0])
        else:
            result = sorted_t_list[0][0]
    else:
        result = sorted_t_list[0][0]

print(result)
