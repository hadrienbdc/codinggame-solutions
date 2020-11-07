import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
words = []
for i in range(n):
    w = input()
    words.append(w)

letters = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

possible = []
for word in words:
    possible.append(word)
    letters_2 = letters
    for l in word:
        if l not in letters_2:
            possible.pop()
            break
        else:
            letters_2 = letters_2.replace(l, '', 1)

dict_point = {'e':1, 'a':1, 'i':1, 'o':1 , 'n':1, 'r':1, 't':1, 'l':1, 's':1, 'u':1,
              'd':2, 'g':2,
              'b':3, 'c':3, 'm':3, 'p':3,
              'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
              'k':5,
              'j':8, 'x':8,
              'q':10, 'z':10,
}

if len(possible) == 1:
    print(possible[0])
else:
    words_point = []
    for word in possible:
        point = 0
        for l in word:
            point += dict_point[l]
        words_point.append((word, point))

    result = max(words_point, key=lambda x: x[1])
    print(result[0])
