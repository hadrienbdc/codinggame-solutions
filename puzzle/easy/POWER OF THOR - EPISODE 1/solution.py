import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    diff_x = light_x - initial_tx
    diff_y = light_y - initial_ty
    print(diff_y, file=sys.stderr)

    # A single line providing the move to be made: N NE E SE S SW W or NW

    if diff_x != 0 and diff_y != 0:
        if diff_x > 0 and diff_y > 0:
            print('SE')
            initial_tx += 1
            initial_ty += 1
        elif diff_x > 0 and diff_y < 0:
            print('NE')
            initial_tx += 1
            initial_ty -= 1
        elif diff_x < 0 and diff_y > 0:
            print('SW')
            initial_tx -= 1
            initial_ty += 1
        elif diff_x < 0 and diff_y < 0:
            print('NW')
            initial_tx -= 1
            initial_ty -= 1
    else:
        if diff_x == 0:
            if diff_y > 0:
                print('S')
                initial_ty += 1
            else:
                print('N')
                initial_ty -= 1
        else:
            if diff_x > 0:
                print('E')
                initial_tx += 1
            else:
                print('W')
                initial_tx -= 1
