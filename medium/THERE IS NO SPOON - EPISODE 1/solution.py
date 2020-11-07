import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
table = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    table.append(line)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in range(height):
    for j in range(width):
        node = table[i][j]
        if node == '0':
            res_node = f'{j} {i}'

            res_rn = '-1 -1'
            for j2 in range(j+1, width):
                rn = table[i][j2]
                if rn == '0':
                    res_rn = f'{j2} {i}'
                    break

            res_bn = '-1 -1'
            for i2 in range(i+1, height):
                bn = table[i2][j]
                if bn == '0':
                    res_bn = f'{j} {i2}'
                    break

            print(res_node, res_rn, res_bn)
