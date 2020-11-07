import sys
import math
from copy import deepcopy

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

s = int(input())  # the size of the board
m = int(input())  # the number of moves to be made
board = [''] * s
enemy = {'B': 'W', 'W': 'B'}
print(m, s, file=sys.stderr)


def print_board(board):
    result = []
    for line in board:
        line_s = ''.join(line)
        result.append(line_s)

    result_s = '\n'.join(result)

    return result_s


def remove_stones(l, board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == l:
                if check_stone(board, i, j):
                    board[i][j] = '.'


def check_stone(board, i, j):
    stone = board[i][j]
    count = 0
    result = False
    if i-1 < 0 or board[i-1][j] == enemy[stone]:
        count += 1
    if i+1 >= s or board[i+1][j] == enemy[stone]:
        count += 1
    if j-1 < 0 or board[i][j-1] == enemy[stone]:
        count += 1
    if j+1 >= s or board[i][j+1] == enemy[stone]:
        count += 1

    if count == 4:
        result = True

    return result


def make_groups(board):
    groups = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != '.':
                if not is_alone(board, i, j):
                    if groups:
                        connected = get_connected(board, i, j)
                        find_group = False
                        for group in groups:
                            if connected in group:
                                group.append((i, j))
                                find_group = True

                        if not find_group:
                            groups.append([(i, j)])

                    else:
                        groups.append([(i, j)])

    return groups


def is_alone(board, i, j):
    stone = board[i][j]
    count = 0
    result = True
    if i-1 >= 0 and board[i-1][j] == stone:
        count += 1
    if i+1 < s and board[i+1][j] == stone:
        count += 1
    if j-1 >= 0 and board[i][j-1] == stone:
        count += 1
    if j+1 < s and board[i][j+1] == stone:
        count += 1

    if count != 0:
        result = False

    return result


def get_connected(board, i, j):
    stone = board[i][j]
    if i-1 >= 0 and board[i-1][j] == stone:
        return i-1, j
    if j-1 >= 0 and board[i][j-1] == stone:
        return i, j-1


def remove_groups(l, board, groups):
    for group in groups:
        count = 0
        for stone in group:
            i, j = stone
            if check_stone_group(board, i, j):
                count += 1
        if count == len(group) and len(group) > 1 and board[i][j] == l:
            for stone in group:
                i, j = stone
                board[i][j] = '.'


def check_stone_group(board, i, j):
    count = 0
    result = False
    if i-1 < 0 or board[i-1][j] != '.':
        count += 1
    if i+1 >= s or board[i+1][j] != '.':
        count += 1
    if j-1 < 0 or board[i][j-1] != '.':
        count += 1
    if j+1 >= s or board[i][j+1] != '.':
        count += 1

    if count == 4:
        result = True

    return result


for i in range(s):
    row = input()  # a single row in the input board
    board[i] = list(row)

not_valid_flag = False
history = []
for i in range(m):
    l, i, j = input().split()  # a strng representation of a move
    i = int(i)
    j = int(j)
    print(l, i, j, file=sys.stderr)
    history.append(deepcopy(board))
    if board[i][j] == '.':
        board[i][j] = l
        groups = make_groups(board)
        for group in groups:
            print(group, file=sys.stderr)

        remove_stones(enemy[l], board)
        remove_groups(enemy[l], board, groups)

        remove_stones(l, board)
        remove_groups(l, board, groups)

        print(print_board(board), file=sys.stderr)
        if board[i][j] == '.':
            not_valid_flag = True
            print('SUICIDAL MOVE', file=sys.stderr)
            break

        if board in history:
            not_valid_flag = True
            print('KO RULES', file=sys.stderr)
            break
    else:
        not_valid_flag = True
        print('FIELD NOT FREE', file=sys.stderr)
        break

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
if not_valid_flag:
    print("NOT_VALID")
else:
    print(print_board(board))
# print("NOT_VALID | <<the_board_after_the_moves>>")
