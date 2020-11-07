import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

dict_cart = {'2': 1,'3': 2,'4': 3,'5': 4,'6': 5,'7': 6 ,'8': 7 ,'9': 10,
             '10': 11,'J': 12,'Q': 13,'K': 14,'A': 15}

n = int(input())  # the number of cards for player 1
l1 = []
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    l1.append(cardp_1)

m = int(input())  # the number of cards for player 2
l2 = []
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    l2.append(cardp_2)

count = 0
win1 = []
win2 = []
result = None
while len(l1) > 0 and len(l2) > 0:
    c1 = l1.pop(0)[:-1]
    c2 = l2.pop(0)[:-1]

    win1.append(c1 + 'X') 
    win2.append(c2 + 'X')

    if dict_cart[c1] > dict_cart[c2]:
        l1.extend(win1 + win2)

        del win1[:]
        del win2[:]
        count += 1
    elif dict_cart[c1] < dict_cart[c2]:
        l2.extend(win1 + win2)

        del win1[:]
        del win2[:]
        count += 1
    else:
        if len(l1) > 3 and len(l2) > 3:
            for i in range(3):
                win1.append(l1.pop(0)[:-1] + 'X') 
                win2.append(l2.pop(0)[:-1] + 'X')
        else:
            result = 'PAT'
            break

if not result:
    if len(l1) == 0:
        print('2', count)
    else:
        print('1', count)
else:
    print(result)
