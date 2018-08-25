from itertools import combinations
from os import system
i = 1
for item in combinations('ABCDEFGHIJKL', 3):
    for item2 in combinations('123456789', 4):
        if i < 21:
            A = []
            position2 = 1
            while position2 < 10:
                if position2 == int(item2[0]) or position2 == int(item2[1]) or position2 == int(item2[2]) or position2 == int(item2[3]):
                    A.append('3')
                else:
                    A.append('4')
                position2 += 1
            tempposition = 'A'
            j = 0
            print(i, end = ': ')
            while ord(tempposition) < 77:
                if tempposition == item[0] or tempposition == item[1] or tempposition == item[2]:
                    print('2', end = '')
                else:
                    print(A[j], end = '')
                    j += 1
                tempposition = chr(ord(tempposition) + 1)
            print()
        i += 1
system("pause")
