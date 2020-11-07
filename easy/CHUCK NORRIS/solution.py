import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
message_b = "".join(f"{ord(i):07b}" for i in message)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
last_char = message_b[0]
result = '00 0' if last_char == '0' else '0 0'
for n in message_b[1:]:
    if n == last_char:
        result += '0'
    else:
        if n == '0':
            result += ' 00 0'
        else:
            result += ' 0 0'

    last_char = n

print(result)
